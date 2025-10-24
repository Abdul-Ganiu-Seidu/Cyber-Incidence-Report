from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ReportForm
from .models import Report
from django.contrib.auth.decorators import login_required

def report_list(request):
    reports = Report.objects.all().order_by('-created_at')
    return render(request, 'reports/report_list.html', {'reports': reports})

def create_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Report submitted successfully.")
            return redirect('report_list')
    else:
        form = ReportForm()
    return render(request, 'reports/create_report.html', {'form': form})

# Admin dashboard - protect with login_required
@login_required
def admin_dashboard(request):
    reports = Report.objects.all().order_by('-created_at')
    return render(request, 'reports/admin_dashboard.html', {'reports': reports})

@login_required
def delete_report(request, pk):
    report = get_object_or_404(Report, pk=pk)
    report.delete()
    messages.warning(request, "Report deleted successfully.")
    return redirect('admin_dashboard')
