#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "argo_project.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
    
    def myview(request):
        rows = MyModel.objects.using('mysql').all()
        return render_to_response("modelinfo.html", {"rows" : rows })