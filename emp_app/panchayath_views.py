from django.contrib import messages
from django.shortcuts import render, redirect

from emp_app.forms import ScheduleAdd
from emp_app.models import Notification, AddScheme, AppointmentSchedule, Panchayath, Appointment


def notification(request):
    data = Notification.objects.all()
    return render(request,'panchayath/notifications.html',{'data':data})



def view_scheme(request):
    data = AddScheme.objects.all()
    return render(request,'panchayath/schemes.html', {'data': data})


def schedule_add(request):
    s = request.user
    u = Panchayath.objects.get(user=s)
    print(u)
    form = ScheduleAdd()
    if request.method == 'POST':
        form = ScheduleAdd(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request, 'Job Added Successfully')
            return redirect('schedule_view')
    else:
        form = ScheduleAdd()
    return render(request, 'panchayath/schedule_add.html', {'form': form})


def schedule(request):
    n = AppointmentSchedule.objects.all()

    context = {
        'schedule': n,

    }
    return render(request, 'panchayath/schedule_view.html', context)


def schedule_delete(request, id):
    data = AppointmentSchedule.objects.get(id=id)
    data.delete()
    messages.info(request, ' Deleted Successfully')
    return redirect('schedule_view')




def appointment_panchayath(request):
    u = request.user
    panchayath = Panchayath.objects.get(user = u)
    print(panchayath)
    p = Appointment.objects.filter(schedule__user=panchayath)


    context = {
        'appointment': p,
     }
    return render(request, 'panchayath/appointment.html', context)




def approve_appointment(request, id):
    n = Appointment.objects.get(id=id)
    n.status = 1
    n.save()
    messages.info(request, 'Approved')
    return redirect('appointment_panchayath')


def reject_appointment(request, id):
    n = Appointment.objects.get(id=id)
    n.status = 2
    n.save()
    messages.info(request,'Rejected')
    return redirect('appointment_panchayath')



