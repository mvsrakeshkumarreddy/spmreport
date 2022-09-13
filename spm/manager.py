from django.contrib.auth.base_user import BaseUserManager



class UserManager(BaseUserManager):
    use_in_migrations = True



    def create_user(self, full_name, crew_ID, station,employee_ID,appointment_date, password=None, **extra_fields):

        if not full_name:
            raise ValueError('full_name is required')

        #full_name = self.normalize_full_name(full_name)
        #some = self.normalize_some(some)
        #crew_ID = crew_ID.upper()
        user = self.model(full_name = full_name, crew_ID = crew_ID, station = station, employee_ID = employee_ID,appointment_date=appointment_date, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, crew_ID, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        full_name = "mvs rakesh kumar"
        station = "SA"
        employee_ID = "1529803601"
        appointment_date = "2022-02-02"

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('super user must have is_staff true'))

        return self.create_user(full_name, crew_ID, station,employee_ID, appointment_date,password, **extra_fields)