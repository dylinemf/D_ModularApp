from django.shortcuts import render, redirect, get_object_or_404
from .models import ManagedModule
from django.core.management import call_command
from modular_project.settings import COMMANDS, AVAILABLE_MODULES

def home(request):
    return render(request, 'modules/home.html')

def modules_dashboard(request):
    for mod in AVAILABLE_MODULES:
        obj, created = ManagedModule.objects.get_or_create(
            name=mod['name'],
            defaults={'label': mod['label'], 'app_name': mod['app_name']}
        ) # could debug obj, created if it is needed
    modules = ManagedModule.objects.all()
    return render(request, 'modules/dashboard.html', {'modules': modules})

# Install action
def install_module(request, pk):
    module = get_object_or_404(ManagedModule, pk=pk)
    if not module.installed:
        # migrate
        call_command(COMMANDS[0], module.app_name)
        call_command(COMMANDS[1], module.app_name)
        module.installed = True
        module.save()
    return redirect('modules-dashboard')

# Uninstall action (disable)
def uninstall_module(request, pk):
    module = get_object_or_404(ManagedModule, pk=pk)
    if module.installed:
        module.installed = False
        module.save()
        # Not really uninstall it from `INSTALLED_APPS`, just disable it from feature
    return redirect('modules-dashboard')

# Upgrade action (auto makemigrations+migrate)
def upgrade_module(request, pk):
    module = get_object_or_404(ManagedModule, pk=pk)
    call_command(COMMANDS[0], module.app_name)
    call_command(COMMANDS[1], module.app_name)
    return redirect('modules-dashboard')