from django.shortcuts import render
from django.http import HttpResponse
import serial
from threading import Thread

def myview(request):
    conn = MySQLdb.connect("connecting to argo...")
    try:
        cursor = conn.cursor()
        cursor.execute("select * from argo.steps")
        # rows = cursor.fetchall()
        
        # now = {{item.field1}}
        currentStep = cursor.fetchone()
        maxSteps = cursor.fetchone()
        modelName = cursor.fetchone()
    finally:
        conn.close()
    
    return render_to_response(html, {"rows" : rows})

    html = "" \
    "<html>" \
    "<head>" \
    "<title>Argo Web Server</title>" \
    "</head>" \
    "<body>You are building: %s." % modelName + \
    "<br>Your current step is: %d." % currentStep + \
    "<br>Maximum # of steps: %d." % maxSteps + \
    "</body>" \
    "</html>"
    return HttpResponse(html)