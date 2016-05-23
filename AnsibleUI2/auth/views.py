#!/usr/bin/env python
# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
from django.http import HttpResponseRedirect
import django.contrib.auth.views
from django.core import urlresolvers
from django.contrib.auth import login
from django.shortcuts import render_to_response as render
from django.template import RequestContext
from django.contrib import auth

LOG = logging.getLogger(__name__)


def login_not_required(func):
    func.login_not_required = True
    return func


@login_not_required
def dt_login(request):
    redirect_to = request.GET.get('next', '/')
    if request.method == 'POST':
        data = request.POST
        if "username" in data and "password" in data:
            username = data.get("username")
            password = data.get("password")
            redirect_to = data.get("next")

        if "rememberme" not in data:
            request.session.set_expiry(0)

        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                login(request, user)
                if request.session.test_cookie_worked():
                    request.session.delete_test_cookie()
                return HttpResponseRedirect(redirect_to)

    else:
        request.session.set_test_cookie()

    return render('login.html', {
        'action': urlresolvers.reverse('login'),
        'next': redirect_to,
        'login_errors': request.method == 'POST',},
        context_instance=RequestContext(request)
    )


def dt_logout(request, next_page=None):
    """Log out the user"""
    return django.contrib.auth.views.logout(request, next_page)
