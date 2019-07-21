from django.shortcuts import render, redirect
from .models import Spare
from django.http import HttpResponse
import json


# Create your views here.
def index(request):
    return render(request, 'spares/index.html')


def sheet(request):
    return render(request, "spares/sheet.html")


def datatables(request):
    users_list = []
    res = Spare.objects.all()
    print(res)

    def if_hurry(item):
        if item.即用备用:
            return "即用"
        return "备用"

    def if_pic(item):
        if str(item.是否有图片附件):
            return "有"
        return "无"

    for item in res:
        user_info = {
            "id号": item.id,
            "申购时间": str(item.申购时间),
            "零件名称": item.零件名称,
            "设备名称": item.设备名,
            "资产类型": item.资产类型,
            "型号": item.型号,
            "品牌": item.品牌,
            "详细细节": item.详细细节,
            "数量": item.数量,
            "单位": item.单位,
            "用途": item.用途,
            "采购人": item.采购人,
            "申购人": item.申购人,
            "即用备用": if_hurry(item),
            "是否上传图片": if_pic(item),
        }
        users_list.append(user_info)
    user_dic = {}
    print(users_list)
    user_dic["data"] = users_list  # 按照官方文档的格式写
    return HttpResponse(json.dumps(user_dic))


def jump(request):
    getid = request.POST.get('edit')
    change_way = request.POST.get('ed_way')
    if change_way == 'dele':
        dele_msg = f'第{getid}行数据刚被删除。'
        Spare.objects.filter(id=getid).delete()
        return render(request, 'spares/sheet.html', {'dele_msg': dele_msg})
    elif change_way == 'edit':
        row_val = Spare.objects.get(pk=getid)
        return render(request, 'spares/reedit.html', {'getid': getid, 'row_val': row_val})
    else:
        return render(request, 'spares/addrow.html', {'getid': getid})


def reedit(request):
    try:
        getid = request.GET.get('getid')
        Spare.objects.filter(id=getid).update(
            申购时间=request.POST.get('apply_time'),
            零件名称=request.POST.get('spare_name'),
            设备名=request.POST.get('equip_name'),
            资产类型=request.POST.get('asset'),
            型号=request.POST.get('mod_number'),
            品牌=request.POST.get('brand'),
            详细细节=request.POST.get('detail'),
            数量=request.POST.get('number'),
            单位=request.POST.get('unit'),
            用途=request.POST.get('usage'),
            采购人=request.POST.get('applyer'),
            申购人=request.POST.get('user'),
            即用备用=request.POST.get('hurry'),
            是否有图片附件=request.POST.get('pic'),
        )
    except Exception as e:
        print(e)
        msg = "请全部填写完成后提交。"
        return render(request, 'spares/reedit.html', {'msg': msg})

    edit_msg = f'第{getid}行数据刚被修改'
    return render(request, 'spares/sheet.html', {'edit_msg': edit_msg})


def addrow(request):
    try:
        spare = Spare()
        spare.申购时间 = request.POST.get('apply_time')
        spare.零件名称 = request.POST.get('spare_name')
        spare.设备名 = request.POST.get('equip_name')
        spare.资产类型 = request.POST.get('asset')
        spare.型号 = request.POST.get('mod_number')
        spare.品牌 = request.POST.get('brand')
        spare.详细细节 = request.POST.get('detail')
        spare.数量 = request.POST.get('number')
        spare.单位 = request.POST.get('unit')
        spare.用途 = request.POST.get('usage')
        spare.采购人 = request.POST.get('applyer')
        spare.申购人 = request.POST.get('user')
        spare.即用备用 = request.POST.get('hurry')
        spare.是否有图片附件 = request.POST.get('pic')
        spare.save()
    except Exception as e:
        print(e)
        msg = "请全部填写完成后提交。"
        return render(request, 'spares/addrow.html', {'msg': msg})

    add_msg = "新的数据已被添加。"
    return render(request, 'spares/sheet.html', {'add_msg': add_msg})

def changed(request, getid):
    try:
        #getid = request.GET.get('my_id')
        Spare.objects.filter(pk=getid).update(
            申购时间=request.POST.get('apply_time'),
            零件名称=request.POST.get('spare_name'),
            设备名=request.POST.get('equip_name'),
            资产类型=request.POST.get('asset'),
            型号=request.POST.get('mod_number'),
            品牌=request.POST.get('brand'),
            详细细节=request.POST.get('detail'),
            数量=request.POST.get('number'),
            单位=request.POST.get('unit'),
            用途=request.POST.get('usage'),
            采购人=request.POST.get('applyer'),
            申购人=request.POST.get('user'),
            即用备用=request.POST.get('hurry'),
            是否有图片附件=request.POST.get('pic'),
        )
    except Exception as e:
        print(e)
        print('错我错我东方大道付多多多多多多多多多多多多多多多多多')
        msg = "请全部填写完成后提交。"
        return render(request, 'spares/reedit.html', {'msg': msg})

    edit_msg = f'第{getid}行数据刚被修改'
    print('row id is               ', getid)
    return render(request, 'spares/sheet.html', {'edit_msg': edit_msg})

