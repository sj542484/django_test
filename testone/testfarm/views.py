import re,os
import subprocess
import time
from testfarm.myutils import Utils
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from testfarm.models import EquipmentList
from testfarm.test_program.run import Driver
from multiprocessing import Process

# Create your views here.

def index(request):
    '''首页'''
    return render(request, 'testproject/index.html')

def show_devices(request):
    '''连接设备展示到页面中'''
    content = get_show_phone()
    return render(request, 'testproject/show_devices.html',content)

def inputInfo(request):
    '''获取设备信息并展示到页面进行设备信息录入'''
    dev_list_info = get_phone_online()
    pat = re.compile('(.*?) .*?model:(.*?) ')
    res = pat.findall(dev_list_info[0])
    if res:
        content = {'devices_model': res[0][1],'devices_uuid':res[0][0]}
    else:
        content = {'devices_model':None}
    return render(request,'{}'.format('testproject/input_info.html'),content)

def saveInfo(request):
    '''保存数据'''
    devices_model = request.POST.get('devices_model')
    devices_uuid = request.POST.get('devices_uuid')
    devices_name = request.POST.get('devices_name')
    platformVersion = request.POST.get('platformVersion')
    try:
        db = EquipmentList(equipment_name=devices_name,equipment_model=devices_model,equipment_uuid=devices_uuid,platform_verion=platformVersion)
        db.save()
        return HttpResponse('<script>alert("数据添加成功");location.href="/inputinfo"</script>')
    except Exception as e:
        print(e)
        return HttpResponse('<script>alert("设备已经存在 请更换设备录入");location.href="/inputinfo"</script>')

def startservice(request,e_name,e_uuid,plat_verion):
    '''开始测试'''
    for i in range(1):
        t = Process(target=st,args=(request,e_name,e_uuid,plat_verion))
        t.start()
        time.sleep(0.3)
    content = get_show_phone()
    return render(request, 'testproject/show_devices.html', content)

def st(request,e_name,e_uuid,plat_verion):
    gid = os.getpid()
    EquipmentList.objects.filter(equipment_uuid=e_uuid).update(start_but_statue=1, statue_statue=1, gid=gid)
    # start appium server
    port = Utils().start_appium()


    dr = Driver(uuid=e_uuid, platformVersion=plat_verion, deviceName=e_name)
    file_name = dr.run_cases(port)  # int类型

    content = get_show_phone()
    content['file_name'] = file_name
    return render(request,'testproject/show_devices.html', content)

def stopservice(request,gid,e_uuid):
    '''关闭进程 结束测试'''
    CMD = 'kill -9 {}'.format(gid)
    os.popen(CMD)
    print('kill进程:',CMD)
    EquipmentList.objects.filter(equipment_uuid=e_uuid).update(start_but_statue=0,statue_statue=0,gid=None)
    content = get_show_phone()
    return render(request, 'testproject/show_devices.html', content)

def get_phone_online():
    '''获取连接的设备信息'''
    res = subprocess.Popen('adb devices -l', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
    result, err = res.communicate()
    result = result.decode().replace('List of devices attached\n', '').replace('\n\n', '')
    dev_list_info = result.split('\n')
    return dev_list_info

def get_show_phone():
    '''获取设备列表页展示的设备/信息'''
    dev_list_info = get_phone_online()
    dev_list = []
    if dev_list_info[0]:
        for i in dev_list_info:
            pat = re.compile('(.*?) .*?model:(.*?) ')
            res = pat.findall(i)
            res = EquipmentList.objects.filter(equipment_uuid=res[0][0])
            if res:
                dev_list.append(res[0])
        if dev_list:
            content = {'devices': dev_list, 'len': len(dev_list)}
        else:
            content = {'devices':0}
    else:
        content = {'devices': 1}
    return content

def showreport(request,file_name):
    file_name = file_name.split('./testfarm/')[1]
    return render(request,file_name)