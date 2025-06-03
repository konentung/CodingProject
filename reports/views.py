from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Report, ReportType

@login_required
def report_view(request):
    user = request.user
    report_types = ReportType.objects.all()
    errors = []
    success = False
    if request.method == 'POST':
        report_type_id = request.POST.get('report_type')
        other_report_type = request.POST.get('other_report_type', '').strip()
        report_content = request.POST.get('report_content', '').strip()
        report_type = None
        if not report_type_id:
            errors.append('請選擇回報類型。')
        else:
            try:
                report_type = ReportType.objects.get(id=report_type_id)
            except ReportType.DoesNotExist:
                errors.append('請選擇有效的回報類型。')
        if report_type and report_type.name == '其他' and not other_report_type:
            errors.append('請填寫其他回報類型。')
        if not report_content:
            errors.append('請填寫問題內容。')
        if not errors and report_type:
            Report.objects.create(
                user=user,
                report_type=report_type,
                other_report_type=other_report_type if report_type.name == '其他' else None,
                report_content=report_content
            )
            request.session['contact_success'] = True
            next_url = request.GET.get('next') or 'ContactUs'
            return redirect(next_url)
    if request.session.pop('contact_success', None):
        success = True
    return render(request, 'report/report.html', locals())
