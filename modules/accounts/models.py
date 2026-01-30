"""
Accounts module: User, Role, Provider, Client.
Table/column names match existing MySQL schema (Sequelize).
"""
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Role(models.Model):
    """Role model - table: roles"""
    role_name = models.CharField(max_length=255, unique=True, null=False, db_column='roleName')
    is_provider = models.BooleanField(default=False, db_column='isProvider')
    is_client = models.BooleanField(default=False, db_column='isClient')
    is_system_user = models.BooleanField(default=False, db_column='isSystemUser')
    is_active = models.BooleanField(default=True, db_column='isActive')
    is_deleted = models.BooleanField(default=False, db_column='isDeleted')
    created_by = models.IntegerField(null=True, blank=True, db_column='createdBy')
    updated_by = models.IntegerField(null=True, blank=True, db_column='updatedBy')
    created_at = models.DateTimeField(auto_now_add=True, db_column='createdAt')
    updated_at = models.DateTimeField(auto_now=True, db_column='updatedAt')

    class Meta:
        db_table = 'roles'
        managed = True


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    """Custom User - table: users. Matches Sequelize User schema."""
    username = models.CharField(max_length=255, null=True, blank=True, unique=True, db_column='username')
    first_name = models.CharField(max_length=255, null=True, blank=True, db_column='firstName')
    last_name = models.CharField(max_length=255, null=True, blank=True, db_column='lastName')
    email = models.EmailField(unique=True, db_column='email')
    facebook_id = models.CharField(max_length=255, null=True, blank=True, db_column='facebookId')
    dob = models.DateField(null=True, blank=True, db_column='dob')
    GENDER_CHOICES = [('male', 'Male'), ('female', 'Female'), ('others', 'Others')]
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True, blank=True, db_column='gender')
    nationality = models.CharField(max_length=255, null=True, blank=True, db_column='nationality')
    AUTH_STRATEGY_CHOICES = [('local', 'Local'), ('facebook', 'Facebook'), ('google', 'Google'), ('apple', 'Apple'), ('twitter', 'Twitter')]
    auth_strategy = models.CharField(max_length=20, choices=AUTH_STRATEGY_CHOICES, default='local', db_column='authStrategy')
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True, related_name='users', db_column='roleId')
    profile_picture = models.CharField(max_length=500, null=True, blank=True, db_column='profilePicture')
    phone_number = models.CharField(max_length=50, null=True, blank=True, db_column='phoneNumber')
    email_verified = models.BooleanField(default=False, db_column='emailVerified')
    phone_verified = models.BooleanField(default=False, db_column='phoneVerified')
    is_profile_completed = models.BooleanField(default=False, db_column='isProfileCompleted')
    ACCOUNT_STATUS_CHOICES = [('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('suspended', 'Suspended')]
    account_status = models.CharField(max_length=20, choices=ACCOUNT_STATUS_CHOICES, default='pending', db_column='accountStatus')
    country_id = models.IntegerField(null=True, blank=True, db_column='countryId')
    county_id = models.IntegerField(null=True, blank=True, db_column='countyId')
    state_id = models.IntegerField(null=True, blank=True, db_column='stateId')
    city_id = models.IntegerField(null=True, blank=True, db_column='cityId')
    zip_code = models.CharField(max_length=20, null=True, blank=True, db_column='zipCode')
    is_online = models.BooleanField(default=False, db_column='isOnline')
    last_login_time = models.DateTimeField(null=True, blank=True, db_column='lastLoginTime')
    latitude = models.FloatField(null=True, blank=True, db_column='latitude')
    longitude = models.FloatField(null=True, blank=True, db_column='longitude')
    is_active = models.BooleanField(default=False, db_column='isActive')
    is_deleted = models.BooleanField(default=False, db_column='isDeleted')
    address = models.TextField(null=True, blank=True, db_column='address')
    apple_user_id = models.CharField(max_length=255, null=True, blank=True, db_column='appleUserId')
    mailing_address = models.CharField(max_length=500, null=True, blank=True, db_column='mailingAddress')
    created_by = models.IntegerField(null=True, blank=True, db_column='createdBy')
    updated_by = models.IntegerField(null=True, blank=True, db_column='updatedBy')
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, db_column='createdAt')
    updated_at = models.DateTimeField(auto_now=True, db_column='updatedAt')

    USERNAME_FIELD = 'email'

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = 'users'
        managed = True


class Provider(models.Model):
    """Provider - table: providers"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='provider', db_column='userId')
    state_bar_number = models.CharField(max_length=255, null=True, blank=True, db_column='stateBarNumber')
    proof_of_malpractice_insurance = models.CharField(max_length=500, null=True, blank=True, db_column='proofOfMalpracticeInsurance')
    APPEARANCE_CHOICES = [('in-person', 'In Person'), ('remote-only', 'Remote Only'), ('both', 'Both')]
    appearance_availability = models.CharField(max_length=20, choices=APPEARANCE_CHOICES, null=True, blank=True, db_column='appearanceAvailability')
    proof_of_paralegal_certification = models.CharField(max_length=500, null=True, blank=True, db_column='proofOfParalegalCertification')
    attorney_verification_letter = models.CharField(max_length=500, null=True, blank=True, db_column='attorneyVerificationLetter')
    proof_of_certification = models.CharField(max_length=500, null=True, blank=True, db_column='proofOfCertification')
    proof_of_business_license = models.CharField(max_length=500, null=True, blank=True, db_column='proofOfBusinessLicense')
    YEARS_CHOICES = [('1-10', '1-10'), ('11-20', '11-20'), ('21-30', '21-30'), ('30+', '30+')]
    years_of_practice = models.CharField(max_length=20, choices=YEARS_CHOICES, null=True, blank=True, db_column='yearsOfPractice')
    office_address = models.CharField(max_length=500, null=True, blank=True, db_column='officeAddress')
    office_address2 = models.CharField(max_length=255, null=True, blank=True, db_column='officeAddress2')
    terms_of_agreement = models.CharField(max_length=500, null=True, blank=True, db_column='termsOfAgreement')
    total_reviews = models.IntegerField(default=0, db_column='totalReviews')
    average_rating = models.FloatField(default=0, db_column='averageRating')
    is_unlimited_case_view = models.BooleanField(default=False, db_column='isUnlimitedCaseView')
    case_view_limit = models.IntegerField(default=0, db_column='caseViewLimit')
    NOTARY_CHOICES = [('client-to-notary', 'Client to Notary'), ('notary-to-client', 'Notary to Client'), ('both', 'Both')]
    notary_service_travel_type = models.CharField(max_length=30, choices=NOTARY_CHOICES, null=True, blank=True, db_column='notaryServiceTravelType')
    is_trial_used = models.BooleanField(default=False, db_column='isTrialUsed')
    has_provider_payment_info = models.BooleanField(default=False, db_column='hasProviderPaymentInfo')
    created_at = models.DateTimeField(auto_now_add=True, db_column='createdAt')
    updated_at = models.DateTimeField(auto_now=True, db_column='updatedAt')

    class Meta:
        db_table = 'providers'
        managed = True


class Client(models.Model):
    """Client - table: clients"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client', db_column='userId')
    additional_details = models.TextField(null=True, blank=True, db_column='additionalDetails')
    identification_number = models.CharField(max_length=255, null=True, blank=True, db_column='identificationNumber')
    emergency_contact_name = models.CharField(max_length=255, null=True, blank=True, db_column='emergencyContactName')
    emergency_contact_number = models.CharField(max_length=50, null=True, blank=True, db_column='emergencyContactNumber')
    marital_status = models.CharField(max_length=50, null=True, blank=True, db_column='maritalStatus')
    spouse_name = models.CharField(max_length=255, null=True, blank=True, db_column='spouseName')
    preferred_language = models.CharField(max_length=50, null=True, blank=True, db_column='preferredLanguage')
    preferred_contact_method = models.CharField(max_length=50, null=True, blank=True, db_column='preferredContactMethod')
    social_media_profiles = models.CharField(max_length=500, null=True, blank=True, db_column='socialMediaProfiles')
    primary_email = models.CharField(max_length=255, null=True, blank=True, db_column='primaryEmail')
    created_at = models.DateTimeField(auto_now_add=True, db_column='createdAt')
    updated_at = models.DateTimeField(auto_now=True, db_column='updatedAt')

    class Meta:
        db_table = 'clients'
        managed = True
