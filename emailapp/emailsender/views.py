import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from django.shortcuts import render, redirect
from .forms import EmailForm

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            smtp_sender = form.cleaned_data['smtp_sender']
            smtp_password = form.cleaned_data['smtp_password']
            email_receiver = form.cleaned_data['receivers']
            cc_receiver = form.cleaned_data.get('cc', '')

            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']

            # Attachments
            attached_file = request.FILES.get('attachment')

            context = ssl.create_default_context()

            try:
                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                    smtp.login(smtp_sender, smtp_password)
                    
                    msg = MIMEMultipart()
                    msg['From'] = smtp_sender
                    msg['To'] = email_receiver
                    msg['Subject'] = subject
                    if cc_receiver:
                        msg['Cc'] = cc_receiver

                    msg.attach(MIMEText(body, 'plain'))

                    if attached_file:
                        filename = attached_file.name
                        attachment = MIMEBase('application', 'octet-stream')
                        attachment.set_payload(attached_file.read())
                        encoders.encode_base64(attachment)
                        attachment.add_header('Content-Disposition', f'attachment; filename={filename}')
                        msg.attach(attachment)

                    smtp.sendmail(smtp_sender, [email_receiver, cc_receiver], msg.as_string())
                    
                return redirect('email_sent')
            except Exception as e:
                return render(request, 'emailsender/email_send_error.html', {'error': str(e)})
    else:
        form = EmailForm()
    return render(request, 'emailsender/send_email.html', {'form': form})

def email_sent(request):
    return render(request, 'emailsender/email_sent.html')

def index(request):
    return render(request, 'emailsender/index.html')