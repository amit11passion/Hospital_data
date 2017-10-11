from datetime import date
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import logout,login
from front_office.cform import DForm
from front_office.labform import LabDetail
from front_office.models import Pdata, Labdata
from front_office.searchform import searchform
from .form import Personalform, PictureForm
from dateutil.relativedelta import relativedelta
import wolframalpha


@login_required
def frontof(request):
    form = Personalform(request.POST or None)
    temperature(request)
    iform = searchform(request.POST)
    # context = {'title': title, 'form': form}

    if form.is_valid():
        if request.method == 'POST' and 'submit' in request.POST:
            patientid = form.cleaned_data['patientid']
            Name = form.cleaned_data['Name']
            DateofBirth = form.cleaned_data['DateofBirth']
            Email = form.cleaned_data['Email']
            Address = form.cleaned_data['Address']
            try:
                obj = Pdata.objects.get(patientid=patientid)
                messages.info(request,'Patientid already exist')
                form = Personalform()
            except Pdata.DoesNotExist:
                delta = relativedelta(date.today(), DateofBirth)
                print(delta.years)
                if(delta.years >100 or delta.years<0):
                    messages.warning(request, 'please enter correct date')
                    form=Personalform()
                    # return render(request, 'frontof.html', {'form': form})
                else:
                    form.save()
                    form=Personalform()
                    # title = "Thank You"
                    # confirm_message = "Your data will be saved."
                    # context = {'title': title, 'confirm_message': confirm_message, }
                    messages.success(request, 'Your data saved')

        if request.method == 'POST' and 'update' in request.POST:
            patientid = form.cleaned_data['patientid']
            Name = form.cleaned_data['Name']
            DateofBirth = form.cleaned_data['DateofBirth']
            Email = form.cleaned_data['Email']
            Address = form.cleaned_data['Address']
            obj = Pdata.objects.get(patientid=patientid)
            obj.Name = Name
            obj.DateofBirth = DateofBirth
            delta = relativedelta(date.today(), DateofBirth)
            obj.Email = Email
            obj.Address = Address
            obj.save()
            if (delta.years > 100 or delta.years < 0):
                messages.warning(request, 'please enter correct date')
                form = Personalform()
            else:
                obj.save()
                form = Personalform()
                messages.success(request, 'Your data updated')
        return render(request, 'frontof.html', {'form': form})
    elif iform.is_valid():
        patientid = iform.cleaned_data['patientid']
        print(str(patientid))
        # handle with try
        obj = None
        try:
            obj = Pdata.objects.get(patientid=patientid)
            print("inside try")
        except Pdata.DoesNotExist:
            print("inside except")
            messages.error(request, 'Patient not Register untill')
            return render(request, 'frontof.html', {'form': form})
            # raise Http404("patientId does not exist")
            # title = "Records not found"
            # return render(request, 'searchforms.html', {'title':title})
        return render(request, 'frontof.html', {'obj': obj, 'iform': iform})

    else:
        return render(request, 'frontof.html', locals())


@login_required
def report(request):
    temperature(request)
    obj = Labdata.objects.select_related("patientid").all()
    print(obj)
    return render(request, 'report.html', {'obj': obj})


def temperature(request):
    app_id = "ALYU56-4KLQTPY8WJ"
    ques = "plano temperature"
    client = wolframalpha.Client(app_id)
    res = client.query(ques)
    answer = next(res.results)
    temp1 = answer.text.split("\n")
    temp=temp1[0]
    print(temp)
    messages.success(request, temp,extra_tags="temp")
    return render(request,'navbar.html', locals())


@login_required
def home(request):
    if request.user.username=='recp':
     return HttpResponseRedirect(reverse('frontof'))
    elif request.user.username=='mgmt':
        return HttpResponseRedirect(reverse('report'))
    elif request.user.username=='labt':
        return HttpResponseRedirect(reverse('medicallab'))
    elif request.user.username=='medp':
        return HttpResponseRedirect(reverse('medicalp'))


@login_required
def medicallab(request):
    temperature(request)
    lform = LabDetail(request.POST or None)
    po=None
    if lform.is_valid():
        if request.method == 'POST' and 'submit' in request.POST:
            PatientId = request.POST['PatientId']
            BloodGlucoseRange = request.POST['BloodGlucoseRange']
            BloodPressure = request.POST['BloodPressure']
            HeartRates = request.POST['HeartRates']
            SkinThikness = request.POST['SkinThikness']
            PragnencyParYear = request.POST['PragnencyParYear']

            try:
                po = Pdata.objects.get(patientid=PatientId)
                try:
                  so=Labdata.objects.get(patientid=po)
                  messages.info(request, 'lab record for this patient exist', extra_tags="lexist")
                  lform = Personalform()
                  return render(request, 'medicallab.html', {'lform': lform})
                except Labdata.DoesNotExist:
                    pass
            except Pdata.DoesNotExist:
                messages.info(request, 'Patientid not yet register',extra_tags="pexist")
                lform = Personalform()
                return render(request, 'medicallab.html', {'lform': lform})

            lb = Labdata(
                    patientid=po,
                    BloodGlucoseRange=BloodGlucoseRange,
                    BloodPressure=BloodPressure,
                    HeartRates=HeartRates,
                    SkinThikness=SkinThikness,
                    PragnencyParYear=PragnencyParYear,

            )
            lb.save(force_insert=True)
            lform=LabDetail()
            messages.info(request, 'Lab data save successfully', extra_tags="psave")

        if request.method == 'POST' and 'update' in request.POST:
            PatientId = request.POST['PatientId']
            BloodGlucoseRange = request.POST['BloodGlucoseRange']
            BloodPressure = request.POST['BloodPressure']
            HeartRates = request.POST['HeartRates']
            SkinThikness = request.POST['SkinThikness']
            PragnencyParYear = request.POST['PragnencyParYear']

            try:
                po = Pdata.objects.get(patientid=PatientId)
                # try:
                #     so = Labdata.objects.get(patientid=po)
                #     messages.info(request, 'lab record for this patient exist', extra_tags="lexist")
                #     lform = Personalform()
                #     return render(request, 'medicallab.html', {'lform': lform})
                # except Labdata.DoesNotExist:
                #     pass
            except Pdata.DoesNotExist:
                messages.info(request, 'Patientid not yet register', extra_tags="pexist")
                lform = Personalform()
                return render(request, 'medicallab.html', {'lform': lform})
            so = Labdata.objects.get(patientid=po)
            so.patientid=po
            so.BloodGlucoseRange=BloodGlucoseRange
            so.BloodPressure=BloodPressure
            so.HeartRates=HeartRates
            so.SkinThikness=SkinThikness
            so.PragnencyParYear=PragnencyParYear
            so.save()
            # lb = Labdata(
            #     patientid=po,
            #     BloodGlucoseRange=BloodGlucoseRange,
            #     BloodPressure=BloodPressure,
            #     HeartRates=HeartRates,
            #     SkinThikness=SkinThikness,
            #     PragnencyParYear=PragnencyParYear,
            #
            # )
            # lb.save(force_insert=True)
            lform = LabDetail()
            messages.info(request, 'Lab data update successfully', extra_tags="lupdate")

    return render(request, 'medicallab.html', {'lform':lform})


@login_required
def medicalp(request):
   temperature(request)
   mform = searchform(request.POST)
   # Dform = DForm(request.POST)
   obj=None
   pids=None
   # print(obj)
   if mform.is_valid():
         patientid = mform.cleaned_data['patientid']
         try:
             pids = Pdata.objects.get(patientid=patientid)
         except Pdata.DoesNotExist:
             messages.error(request, 'Patient not register yet', extra_tags="pnot")
             mform=searchform()
             return render(request, 'medicalp.html', {'mform': mform})

         try:
            obj = Labdata.objects.select_related("patientid").get(patientid=pids.pk)
         except Labdata.DoesNotExist:
             messages.error(request, 'Patient lab Data not present', extra_tags="lnot")
             mform=searchform()
             return render(request, 'medicalp.html', {'mform': mform})
         return redirect('medicaldecision', patient_id=pids.pk)
   return render(request, 'medicalp.html', {'obj': obj, 'mform': mform})
   # elif Dform.is_valid():
   #       if 'diabe' in request.POST:
   #              did = request.POST['diabe']
   #              print(did)
   #              obj.Diabetes = did
   #              obj.save()
   #              messages.info(request, 'Data update successfully', extra_tags="dupdate")
   #              print('form was valid')
   #              return render(request, 'medicalp.html', {'Dform': Dform})
   #       else:
   #           print("in else")
   #       return rendter(request, 'medicalp.html', {'Dform': Dform})
   # print("outside if")



@login_required
def medicaldecision(request, patient_id):
    temperature(request)
    obj = Labdata.objects.select_related("patientid").get(patientid=patient_id)
    form = PictureForm(request.POST)
    a = None
    if form.is_valid():
        # a = form.cleaned_data['like']
        pdetail = Labdata.objects.get(pk=obj.id)
        pdetail.Diabetes=form.cleaned_data['analyses']
        pdetail.save()
        form=PictureForm()
        messages.success(request, 'Lab data update successfully', extra_tags="laupdate")
        return redirect('medicalp')
    return render(request, 'medicaldecision.html', {'form': form,'obj':obj})

def logout_view(request):
    logout(request)
    # return redirect('/front_office/login')
    return render(request, 'logout.html', {'login':login})


# def search(request):
#     print("search")
#     iform = searchform(request.POST)
#     print(iform)
#     if iform.is_valid():
#          patientid = iform.cleaned_data['patientid']
#          print(str(patientid))
#          #handle with try
#          try:
#               obj = Pdata.objects.get(patientid=int(patientid))
#               print("inside try")
#               # print(obj)
#               # return render(request, 'searchforms.html', {'form':form,'obj': obj})
#          except Pdata.DoesNotExist:
#               print("inside except")
#               raise Http404("patientId does not exist")
#               # title = "Records not found"
#               # return render(request, 'searchforms.html', {'title':title})
#          return render(request, 'frontof.html',  {'obj': obj,'iform':iform})
#     else:
#         return render(request, 'frontof.html', locals())





