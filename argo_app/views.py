import MySQLdb
from django.shortcuts import render
from django.http import HttpResponse
from threading import Thread
import json

modelid = ""

def getDataFromServer(request):
    conn = MySQLdb.connect("localhost", "django_user", "p@ssword", "argo")
    query = "select currentStep, maxSteps, modelName, hasError, rotValue from argo.argo_app_steps where modelName= '%s'" % modelid
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        step = cursor.fetchall()
        print "***** pulling data *****"
        print query
        #for row in step:
         #   print(row[0])
        #    print(row[1])
        
    finally:
        conn.close()
    
    # return render_to_response(html, {"rows" : rows})
    data="iyak"
    
    if request.method == 'GET':
        data = "{ 'data': [{ "
        for row in step:
            data += "'currentStep' : '%d', " % row[0]
            data += "'maxStep' = '%d', " % row[1]
            data += "'modelName' : '%s', " % row[2]
            data += "'hasError' : '%d'," % row[3]
            data += "'rotValue' : '%s'" % row[4]
        data += " }] }"
        
        return HttpResponse(json.dumps(data).strip('"'), content_type='application/json')
    
    return HttpResponse(json.dumps(data), content_type='application/json')

def getModelFromApp(request):
    global modelid
    if request.method == 'GET':
        modelid = request.GET.get('id')
        print "***** setting model *****"
        print modelid
        conn = MySQLdb.connect("localhost", "django_user", "p@ssword", "argo")
        query = "update argo_app_steps set modelSelected=1 where modelName='%s'" % modelid
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            print query
            conn.commit()
            conn.close()
            
            conn = MySQLdb.connect("localhost", "django_user", "p@ssword", "argo")
            query = "select modelName, modelSelected from argo_app_steps where modelName='%s'" % modelid
            cursor = conn.cursor()
            cursor.execute(query)
            step = cursor.fetchall()
            data=""
            for row in step:
                data += "modelName: %s  " % row[0]
                data += "modelSelected: %d" % row[1]
            print query
            print data
            
        finally:
            conn.close()
    return HttpResponse(modelid)

def getModelFromDb():
    global modelid
    try:                        
        conn = MySQLdb.connect("localhost", "django_user", "p@ssword", "argo")
        query = "select modelName from argo_app_steps where modelSelected=1"
        cursor = conn.cursor()
        cursor.execute(query)
        step = cursor.fetchall()
        for row in step:
            modelid = row[0]
        print query
        print modelid

    finally:
        conn.close()
    return modelid

def moveToNextStep(request):
    global modelid
    if request.method == 'GET':
        currentstep = request.GET.get('id')
        print "***** moving to the next step *****"
        modelid = getModelFromDb()
        try:                        
            conn = MySQLdb.connect("localhost", "django_user", "p@ssword", "argo")
            query = "update argo_app_steps set currentStep='%s'+1 " % currentstep
            query += "where modelName='%s'" % modelid
            cursor = conn.cursor()
            cursor.execute(query)
            print query
            conn.commit()
            conn.close()
            
            conn = MySQLdb.connect("localhost", "django_user", "p@ssword", "argo")
            query = "select modelName, currentStep from argo_app_steps where modelName='%s'" % modelid
            cursor = conn.cursor()
            cursor.execute(query)
            step = cursor.fetchall()
            data=""
            for row in step:
                data += "modelName: %s  " % row[0]
                data += "currentStep: %d" % row[1]
            print query
            print data
            
        finally:
            conn.close()
    return HttpResponse(modelid)



def moveToPrevStep(request):
    global modelid
    if request.method == 'GET':
        currentstep = request.GET.get('id')
        print "***** moving to the prev step *****"
        modelid = getModelFromDb()
        try:                        
            conn = MySQLdb.connect("localhost", "django_user", "p@ssword", "argo")
            query = "update argo_app_steps set currentStep='%s'-1 " % currentstep
            query += "where modelName='%s'" % modelid
            cursor = conn.cursor()
            cursor.execute(query)
            print query
            conn.commit()
            conn.close()
            
            conn = MySQLdb.connect("localhost", "django_user", "p@ssword", "argo")
            query = "select modelName, currentStep from argo_app_steps where modelName='%s'" % modelid
            cursor = conn.cursor()
            cursor.execute(query)
            step = cursor.fetchall()
            data=""
            for row in step:
                data += "modelName: %s  " % row[0]
                data += "currentStep: %d" % row[1]
            print query
            print data
            
        finally:
            conn.close()
    return HttpResponse(modelid)
