from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from getpass import getpass

class Command(BaseCommand):
    help = 'Creates a superuser with default parameters'

    def add_arguments(self,parser):
        parser.add_argument('--username',type=str,default='admin',help='Username for the super user (default: admin)')
        parser.add_argument('--email',type=str,default='admin@admin.com',help='Email for the super user(default: admin@admin.com)')
        parser.add_argument('--password',type=str,default=None,help='Password for the superuser(default: will prompt for password)')
    
    def handle(self,*args,**options):

        username = options['username']
        password = options['password']
        email = options['email']

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.ERROR('User with this username already exists'))
            return
        
        if password is None:
            password = getpass('Password: ')
        
        User.objects.create_superuser(username = username, email = email, password = password)
        self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
