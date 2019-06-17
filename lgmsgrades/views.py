from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.conf import settings

from django.urls import reverse

#from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.db.models import Q



from django import forms


import datetime
import time
import logging
# Create your views here.

