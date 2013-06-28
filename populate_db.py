#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated.
# Instead of changing it, create a file called import_helper.py
# which this script has hooks to.
#
# On that file, don't forget to add the necessary Django imports
# and take a look at how locate_object() and save_or_locate()
# are implemented here and expected to behave.
#
# This file was generated with the following command:
# manage.py dumpscript
#
# to restore it, run
# manage.py runscript module_name.this_script_name
#
# example: if manage.py is at ./manage.py
# and the script is at ./some_folder/some_script.py
# you must make sure ./some_folder/__init__.py exists
# and run  ./manage.py runscript some_folder.some_script


IMPORT_HELPER_AVAILABLE = False
try:
    import import_helper
    IMPORT_HELPER_AVAILABLE = True
except ImportError:
    pass

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

def run():
    #initial imports

    def locate_object(original_class, original_pk_name, the_class, pk_name, pk_value, obj_content):
        #You may change this function to do specific lookup for specific objects
        #
        #original_class class of the django orm's object that needs to be located
        #original_pk_name the primary key of original_class
        #the_class      parent class of original_class which contains obj_content
        #pk_name        the primary key of original_class
        #pk_value       value of the primary_key
        #obj_content    content of the object which was not exported.
        #
        #you should use obj_content to locate the object on the target db
        #
        #and example where original_class and the_class are different is
        #when original_class is Farmer and
        #the_class is Person. The table may refer to a Farmer but you will actually
        #need to locate Person in order to instantiate that Farmer
        #
        #example:
        #if the_class == SurveyResultFormat or the_class == SurveyType or the_class == SurveyState:
        #    pk_name="name"
        #    pk_value=obj_content[pk_name]
        #if the_class == StaffGroup:
        #    pk_value=8


        if IMPORT_HELPER_AVAILABLE and hasattr(import_helper, "locate_object"):
            return import_helper.locate_object(original_class, original_pk_name, the_class, pk_name, pk_value, obj_content)

        search_data = { pk_name: pk_value }
        the_obj =the_class.objects.get(**search_data)
        return the_obj

    def save_or_locate(the_obj):
        if IMPORT_HELPER_AVAILABLE and hasattr(import_helper, "save_or_locate"):
            the_obj = import_helper.save_or_locate(the_obj)
        else:
            the_obj.save()
        return the_obj



    #Processing model: Permission

    from django.contrib.auth.models import Permission

    auth_permission_1 = Permission()
    auth_permission_1.name = u'Can add log entry'
    auth_permission_1.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_1.codename = u'add_logentry'
    auth_permission_1 = save_or_locate(auth_permission_1)

    auth_permission_2 = Permission()
    auth_permission_2.name = u'Can change log entry'
    auth_permission_2.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_2.codename = u'change_logentry'
    auth_permission_2 = save_or_locate(auth_permission_2)

    auth_permission_3 = Permission()
    auth_permission_3.name = u'Can delete log entry'
    auth_permission_3.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_3.codename = u'delete_logentry'
    auth_permission_3 = save_or_locate(auth_permission_3)

    auth_permission_4 = Permission()
    auth_permission_4.name = u'Can add appointment'
    auth_permission_4.content_type = ContentType.objects.get(app_label="appointments", model="appointment")
    auth_permission_4.codename = u'add_appointment'
    auth_permission_4 = save_or_locate(auth_permission_4)

    auth_permission_5 = Permission()
    auth_permission_5.name = u'Can change appointment'
    auth_permission_5.content_type = ContentType.objects.get(app_label="appointments", model="appointment")
    auth_permission_5.codename = u'change_appointment'
    auth_permission_5 = save_or_locate(auth_permission_5)

    auth_permission_6 = Permission()
    auth_permission_6.name = u'Can delete appointment'
    auth_permission_6.content_type = ContentType.objects.get(app_label="appointments", model="appointment")
    auth_permission_6.codename = u'delete_appointment'
    auth_permission_6 = save_or_locate(auth_permission_6)

    auth_permission_7 = Permission()
    auth_permission_7.name = u'Can add group'
    auth_permission_7.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_7.codename = u'add_group'
    auth_permission_7 = save_or_locate(auth_permission_7)

    auth_permission_8 = Permission()
    auth_permission_8.name = u'Can change group'
    auth_permission_8.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_8.codename = u'change_group'
    auth_permission_8 = save_or_locate(auth_permission_8)

    auth_permission_9 = Permission()
    auth_permission_9.name = u'Can delete group'
    auth_permission_9.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_9.codename = u'delete_group'
    auth_permission_9 = save_or_locate(auth_permission_9)

    auth_permission_10 = Permission()
    auth_permission_10.name = u'Can add permission'
    auth_permission_10.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_10.codename = u'add_permission'
    auth_permission_10 = save_or_locate(auth_permission_10)

    auth_permission_11 = Permission()
    auth_permission_11.name = u'Can change permission'
    auth_permission_11.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_11.codename = u'change_permission'
    auth_permission_11 = save_or_locate(auth_permission_11)

    auth_permission_12 = Permission()
    auth_permission_12.name = u'Can delete permission'
    auth_permission_12.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_12.codename = u'delete_permission'
    auth_permission_12 = save_or_locate(auth_permission_12)

    auth_permission_13 = Permission()
    auth_permission_13.name = u'Can add user'
    auth_permission_13.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_13.codename = u'add_user'
    auth_permission_13 = save_or_locate(auth_permission_13)

    auth_permission_14 = Permission()
    auth_permission_14.name = u'Can change user'
    auth_permission_14.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_14.codename = u'change_user'
    auth_permission_14 = save_or_locate(auth_permission_14)

    auth_permission_15 = Permission()
    auth_permission_15.name = u'Can delete user'
    auth_permission_15.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_15.codename = u'delete_user'
    auth_permission_15 = save_or_locate(auth_permission_15)

    auth_permission_16 = Permission()
    auth_permission_16.name = u'Can add content type'
    auth_permission_16.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_16.codename = u'add_contenttype'
    auth_permission_16 = save_or_locate(auth_permission_16)

    auth_permission_17 = Permission()
    auth_permission_17.name = u'Can change content type'
    auth_permission_17.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_17.codename = u'change_contenttype'
    auth_permission_17 = save_or_locate(auth_permission_17)

    auth_permission_18 = Permission()
    auth_permission_18.name = u'Can delete content type'
    auth_permission_18.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_18.codename = u'delete_contenttype'
    auth_permission_18 = save_or_locate(auth_permission_18)

    auth_permission_19 = Permission()
    auth_permission_19.name = u'Can add division'
    auth_permission_19.content_type = ContentType.objects.get(app_label="drugcompanies", model="division")
    auth_permission_19.codename = u'add_division'
    auth_permission_19 = save_or_locate(auth_permission_19)

    auth_permission_20 = Permission()
    auth_permission_20.name = u'Can change division'
    auth_permission_20.content_type = ContentType.objects.get(app_label="drugcompanies", model="division")
    auth_permission_20.codename = u'change_division'
    auth_permission_20 = save_or_locate(auth_permission_20)

    auth_permission_21 = Permission()
    auth_permission_21.name = u'Can delete division'
    auth_permission_21.content_type = ContentType.objects.get(app_label="drugcompanies", model="division")
    auth_permission_21.codename = u'delete_division'
    auth_permission_21 = save_or_locate(auth_permission_21)

    auth_permission_22 = Permission()
    auth_permission_22.name = u'Can add drug'
    auth_permission_22.content_type = ContentType.objects.get(app_label="drugcompanies", model="drug")
    auth_permission_22.codename = u'add_drug'
    auth_permission_22 = save_or_locate(auth_permission_22)

    auth_permission_23 = Permission()
    auth_permission_23.name = u'Can change drug'
    auth_permission_23.content_type = ContentType.objects.get(app_label="drugcompanies", model="drug")
    auth_permission_23.codename = u'change_drug'
    auth_permission_23 = save_or_locate(auth_permission_23)

    auth_permission_24 = Permission()
    auth_permission_24.name = u'Can delete drug'
    auth_permission_24.content_type = ContentType.objects.get(app_label="drugcompanies", model="drug")
    auth_permission_24.codename = u'delete_drug'
    auth_permission_24 = save_or_locate(auth_permission_24)

    auth_permission_25 = Permission()
    auth_permission_25.name = u'Can add drug company'
    auth_permission_25.content_type = ContentType.objects.get(app_label="drugcompanies", model="drugcompany")
    auth_permission_25.codename = u'add_drugcompany'
    auth_permission_25 = save_or_locate(auth_permission_25)

    auth_permission_26 = Permission()
    auth_permission_26.name = u'Can change drug company'
    auth_permission_26.content_type = ContentType.objects.get(app_label="drugcompanies", model="drugcompany")
    auth_permission_26.codename = u'change_drugcompany'
    auth_permission_26 = save_or_locate(auth_permission_26)

    auth_permission_27 = Permission()
    auth_permission_27.name = u'Can delete drug company'
    auth_permission_27.content_type = ContentType.objects.get(app_label="drugcompanies", model="drugcompany")
    auth_permission_27.codename = u'delete_drugcompany'
    auth_permission_27 = save_or_locate(auth_permission_27)

    auth_permission_28 = Permission()
    auth_permission_28.name = u'Can add drug ndc'
    auth_permission_28.content_type = ContentType.objects.get(app_label="drugcompanies", model="drugndc")
    auth_permission_28.codename = u'add_drugndc'
    auth_permission_28 = save_or_locate(auth_permission_28)

    auth_permission_29 = Permission()
    auth_permission_29.name = u'Can change drug ndc'
    auth_permission_29.content_type = ContentType.objects.get(app_label="drugcompanies", model="drugndc")
    auth_permission_29.codename = u'change_drugndc'
    auth_permission_29 = save_or_locate(auth_permission_29)

    auth_permission_30 = Permission()
    auth_permission_30.name = u'Can delete drug ndc'
    auth_permission_30.content_type = ContentType.objects.get(app_label="drugcompanies", model="drugndc")
    auth_permission_30.codename = u'delete_drugndc'
    auth_permission_30 = save_or_locate(auth_permission_30)

    auth_permission_31 = Permission()
    auth_permission_31.name = u'Can add drug rep'
    auth_permission_31.content_type = ContentType.objects.get(app_label="drugcompanies", model="drugrep")
    auth_permission_31.codename = u'add_drugrep'
    auth_permission_31 = save_or_locate(auth_permission_31)

    auth_permission_32 = Permission()
    auth_permission_32.name = u'Can change drug rep'
    auth_permission_32.content_type = ContentType.objects.get(app_label="drugcompanies", model="drugrep")
    auth_permission_32.codename = u'change_drugrep'
    auth_permission_32 = save_or_locate(auth_permission_32)

    auth_permission_33 = Permission()
    auth_permission_33.name = u'Can delete drug rep'
    auth_permission_33.content_type = ContentType.objects.get(app_label="drugcompanies", model="drugrep")
    auth_permission_33.codename = u'delete_drugrep'
    auth_permission_33 = save_or_locate(auth_permission_33)

    auth_permission_34 = Permission()
    auth_permission_34.name = u'Can add manager'
    auth_permission_34.content_type = ContentType.objects.get(app_label="drugcompanies", model="manager")
    auth_permission_34.codename = u'add_manager'
    auth_permission_34 = save_or_locate(auth_permission_34)

    auth_permission_35 = Permission()
    auth_permission_35.name = u'Can change manager'
    auth_permission_35.content_type = ContentType.objects.get(app_label="drugcompanies", model="manager")
    auth_permission_35.codename = u'change_manager'
    auth_permission_35 = save_or_locate(auth_permission_35)

    auth_permission_36 = Permission()
    auth_permission_36.name = u'Can delete manager'
    auth_permission_36.content_type = ContentType.objects.get(app_label="drugcompanies", model="manager")
    auth_permission_36.codename = u'delete_manager'
    auth_permission_36 = save_or_locate(auth_permission_36)

    auth_permission_37 = Permission()
    auth_permission_37.name = u'Can add bin number'
    auth_permission_37.content_type = ContentType.objects.get(app_label="insurance", model="binnumber")
    auth_permission_37.codename = u'add_binnumber'
    auth_permission_37 = save_or_locate(auth_permission_37)

    auth_permission_38 = Permission()
    auth_permission_38.name = u'Can change bin number'
    auth_permission_38.content_type = ContentType.objects.get(app_label="insurance", model="binnumber")
    auth_permission_38.codename = u'change_binnumber'
    auth_permission_38 = save_or_locate(auth_permission_38)

    auth_permission_39 = Permission()
    auth_permission_39.name = u'Can delete bin number'
    auth_permission_39.content_type = ContentType.objects.get(app_label="insurance", model="binnumber")
    auth_permission_39.codename = u'delete_binnumber'
    auth_permission_39 = save_or_locate(auth_permission_39)

    auth_permission_40 = Permission()
    auth_permission_40.name = u'Can add insuror'
    auth_permission_40.content_type = ContentType.objects.get(app_label="insurance", model="insuror")
    auth_permission_40.codename = u'add_insuror'
    auth_permission_40 = save_or_locate(auth_permission_40)

    auth_permission_41 = Permission()
    auth_permission_41.name = u'Can change insuror'
    auth_permission_41.content_type = ContentType.objects.get(app_label="insurance", model="insuror")
    auth_permission_41.codename = u'change_insuror'
    auth_permission_41 = save_or_locate(auth_permission_41)

    auth_permission_42 = Permission()
    auth_permission_42.name = u'Can delete insuror'
    auth_permission_42.content_type = ContentType.objects.get(app_label="insurance", model="insuror")
    auth_permission_42.codename = u'delete_insuror'
    auth_permission_42 = save_or_locate(auth_permission_42)

    auth_permission_43 = Permission()
    auth_permission_43.name = u'Can add payor'
    auth_permission_43.content_type = ContentType.objects.get(app_label="insurance", model="payor")
    auth_permission_43.codename = u'add_payor'
    auth_permission_43 = save_or_locate(auth_permission_43)

    auth_permission_44 = Permission()
    auth_permission_44.name = u'Can change payor'
    auth_permission_44.content_type = ContentType.objects.get(app_label="insurance", model="payor")
    auth_permission_44.codename = u'change_payor'
    auth_permission_44 = save_or_locate(auth_permission_44)

    auth_permission_45 = Permission()
    auth_permission_45.name = u'Can delete payor'
    auth_permission_45.content_type = ContentType.objects.get(app_label="insurance", model="payor")
    auth_permission_45.codename = u'delete_payor'
    auth_permission_45 = save_or_locate(auth_permission_45)

    auth_permission_46 = Permission()
    auth_permission_46.name = u'Can add interaction'
    auth_permission_46.content_type = ContentType.objects.get(app_label="interactions", model="interaction")
    auth_permission_46.codename = u'add_interaction'
    auth_permission_46 = save_or_locate(auth_permission_46)

    auth_permission_47 = Permission()
    auth_permission_47.name = u'Can change interaction'
    auth_permission_47.content_type = ContentType.objects.get(app_label="interactions", model="interaction")
    auth_permission_47.codename = u'change_interaction'
    auth_permission_47 = save_or_locate(auth_permission_47)

    auth_permission_48 = Permission()
    auth_permission_48.name = u'Can delete interaction'
    auth_permission_48.content_type = ContentType.objects.get(app_label="interactions", model="interaction")
    auth_permission_48.codename = u'delete_interaction'
    auth_permission_48 = save_or_locate(auth_permission_48)

    auth_permission_49 = Permission()
    auth_permission_49.name = u'Can add interaction type'
    auth_permission_49.content_type = ContentType.objects.get(app_label="interactions", model="interactiontype")
    auth_permission_49.codename = u'add_interactiontype'
    auth_permission_49 = save_or_locate(auth_permission_49)

    auth_permission_50 = Permission()
    auth_permission_50.name = u'Can change interaction type'
    auth_permission_50.content_type = ContentType.objects.get(app_label="interactions", model="interactiontype")
    auth_permission_50.codename = u'change_interactiontype'
    auth_permission_50 = save_or_locate(auth_permission_50)

    auth_permission_51 = Permission()
    auth_permission_51.name = u'Can delete interaction type'
    auth_permission_51.content_type = ContentType.objects.get(app_label="interactions", model="interactiontype")
    auth_permission_51.codename = u'delete_interactiontype'
    auth_permission_51 = save_or_locate(auth_permission_51)

    auth_permission_52 = Permission()
    auth_permission_52.name = u'Can add patient'
    auth_permission_52.content_type = ContentType.objects.get(app_label="patients", model="patient")
    auth_permission_52.codename = u'add_patient'
    auth_permission_52 = save_or_locate(auth_permission_52)

    auth_permission_53 = Permission()
    auth_permission_53.name = u'Can change patient'
    auth_permission_53.content_type = ContentType.objects.get(app_label="patients", model="patient")
    auth_permission_53.codename = u'change_patient'
    auth_permission_53 = save_or_locate(auth_permission_53)

    auth_permission_54 = Permission()
    auth_permission_54.name = u'Can delete patient'
    auth_permission_54.content_type = ContentType.objects.get(app_label="patients", model="patient")
    auth_permission_54.codename = u'delete_patient'
    auth_permission_54 = save_or_locate(auth_permission_54)

    auth_permission_55 = Permission()
    auth_permission_55.name = u'Can add batch'
    auth_permission_55.content_type = ContentType.objects.get(app_label="payments", model="batch")
    auth_permission_55.codename = u'add_batch'
    auth_permission_55 = save_or_locate(auth_permission_55)

    auth_permission_56 = Permission()
    auth_permission_56.name = u'Can change batch'
    auth_permission_56.content_type = ContentType.objects.get(app_label="payments", model="batch")
    auth_permission_56.codename = u'change_batch'
    auth_permission_56 = save_or_locate(auth_permission_56)

    auth_permission_57 = Permission()
    auth_permission_57.name = u'Can delete batch'
    auth_permission_57.content_type = ContentType.objects.get(app_label="payments", model="batch")
    auth_permission_57.codename = u'delete_batch'
    auth_permission_57 = save_or_locate(auth_permission_57)

    auth_permission_58 = Permission()
    auth_permission_58.name = u'Can add check'
    auth_permission_58.content_type = ContentType.objects.get(app_label="payments", model="check")
    auth_permission_58.codename = u'add_check'
    auth_permission_58 = save_or_locate(auth_permission_58)

    auth_permission_59 = Permission()
    auth_permission_59.name = u'Can change check'
    auth_permission_59.content_type = ContentType.objects.get(app_label="payments", model="check")
    auth_permission_59.codename = u'change_check'
    auth_permission_59 = save_or_locate(auth_permission_59)

    auth_permission_60 = Permission()
    auth_permission_60.name = u'Can delete check'
    auth_permission_60.content_type = ContentType.objects.get(app_label="payments", model="check")
    auth_permission_60.codename = u'delete_check'
    auth_permission_60 = save_or_locate(auth_permission_60)

    auth_permission_61 = Permission()
    auth_permission_61.name = u'Can add payment transaction'
    auth_permission_61.content_type = ContentType.objects.get(app_label="payments", model="paymenttransaction")
    auth_permission_61.codename = u'add_paymenttransaction'
    auth_permission_61 = save_or_locate(auth_permission_61)

    auth_permission_62 = Permission()
    auth_permission_62.name = u'Can change payment transaction'
    auth_permission_62.content_type = ContentType.objects.get(app_label="payments", model="paymenttransaction")
    auth_permission_62.codename = u'change_paymenttransaction'
    auth_permission_62 = save_or_locate(auth_permission_62)

    auth_permission_63 = Permission()
    auth_permission_63.name = u'Can delete payment transaction'
    auth_permission_63.content_type = ContentType.objects.get(app_label="payments", model="paymenttransaction")
    auth_permission_63.codename = u'delete_paymenttransaction'
    auth_permission_63 = save_or_locate(auth_permission_63)

    auth_permission_64 = Permission()
    auth_permission_64.name = u'Can add payment type'
    auth_permission_64.content_type = ContentType.objects.get(app_label="payments", model="paymenttype")
    auth_permission_64.codename = u'add_paymenttype'
    auth_permission_64 = save_or_locate(auth_permission_64)

    auth_permission_65 = Permission()
    auth_permission_65.name = u'Can change payment type'
    auth_permission_65.content_type = ContentType.objects.get(app_label="payments", model="paymenttype")
    auth_permission_65.codename = u'change_paymenttype'
    auth_permission_65 = save_or_locate(auth_permission_65)

    auth_permission_66 = Permission()
    auth_permission_66.name = u'Can delete payment type'
    auth_permission_66.content_type = ContentType.objects.get(app_label="payments", model="paymenttype")
    auth_permission_66.codename = u'delete_paymenttype'
    auth_permission_66 = save_or_locate(auth_permission_66)

    auth_permission_67 = Permission()
    auth_permission_67.name = u'Can add category'
    auth_permission_67.content_type = ContentType.objects.get(app_label="practices", model="category")
    auth_permission_67.codename = u'add_category'
    auth_permission_67 = save_or_locate(auth_permission_67)

    auth_permission_68 = Permission()
    auth_permission_68.name = u'Can change category'
    auth_permission_68.content_type = ContentType.objects.get(app_label="practices", model="category")
    auth_permission_68.codename = u'change_category'
    auth_permission_68 = save_or_locate(auth_permission_68)

    auth_permission_69 = Permission()
    auth_permission_69.name = u'Can delete category'
    auth_permission_69.content_type = ContentType.objects.get(app_label="practices", model="category")
    auth_permission_69.codename = u'delete_category'
    auth_permission_69 = save_or_locate(auth_permission_69)

    auth_permission_70 = Permission()
    auth_permission_70.name = u'Can add contact type'
    auth_permission_70.content_type = ContentType.objects.get(app_label="practices", model="contacttype")
    auth_permission_70.codename = u'add_contacttype'
    auth_permission_70 = save_or_locate(auth_permission_70)

    auth_permission_71 = Permission()
    auth_permission_71.name = u'Can change contact type'
    auth_permission_71.content_type = ContentType.objects.get(app_label="practices", model="contacttype")
    auth_permission_71.codename = u'change_contacttype'
    auth_permission_71 = save_or_locate(auth_permission_71)

    auth_permission_72 = Permission()
    auth_permission_72.name = u'Can delete contact type'
    auth_permission_72.content_type = ContentType.objects.get(app_label="practices", model="contacttype")
    auth_permission_72.codename = u'delete_contacttype'
    auth_permission_72 = save_or_locate(auth_permission_72)

    auth_permission_73 = Permission()
    auth_permission_73.name = u'Can add doctor'
    auth_permission_73.content_type = ContentType.objects.get(app_label="practices", model="doctor")
    auth_permission_73.codename = u'add_doctor'
    auth_permission_73 = save_or_locate(auth_permission_73)

    auth_permission_74 = Permission()
    auth_permission_74.name = u'Can change doctor'
    auth_permission_74.content_type = ContentType.objects.get(app_label="practices", model="doctor")
    auth_permission_74.codename = u'change_doctor'
    auth_permission_74 = save_or_locate(auth_permission_74)

    auth_permission_75 = Permission()
    auth_permission_75.name = u'Can delete doctor'
    auth_permission_75.content_type = ContentType.objects.get(app_label="practices", model="doctor")
    auth_permission_75.codename = u'delete_doctor'
    auth_permission_75 = save_or_locate(auth_permission_75)

    auth_permission_76 = Permission()
    auth_permission_76.name = u'Can add multi practice'
    auth_permission_76.content_type = ContentType.objects.get(app_label="practices", model="multipractice")
    auth_permission_76.codename = u'add_multipractice'
    auth_permission_76 = save_or_locate(auth_permission_76)

    auth_permission_77 = Permission()
    auth_permission_77.name = u'Can change multi practice'
    auth_permission_77.content_type = ContentType.objects.get(app_label="practices", model="multipractice")
    auth_permission_77.codename = u'change_multipractice'
    auth_permission_77 = save_or_locate(auth_permission_77)

    auth_permission_78 = Permission()
    auth_permission_78.name = u'Can delete multi practice'
    auth_permission_78.content_type = ContentType.objects.get(app_label="practices", model="multipractice")
    auth_permission_78.codename = u'delete_multipractice'
    auth_permission_78 = save_or_locate(auth_permission_78)

    auth_permission_79 = Permission()
    auth_permission_79.name = u'Can add practice'
    auth_permission_79.content_type = ContentType.objects.get(app_label="practices", model="practice")
    auth_permission_79.codename = u'add_practice'
    auth_permission_79 = save_or_locate(auth_permission_79)

    auth_permission_80 = Permission()
    auth_permission_80.name = u'Can change practice'
    auth_permission_80.content_type = ContentType.objects.get(app_label="practices", model="practice")
    auth_permission_80.codename = u'change_practice'
    auth_permission_80 = save_or_locate(auth_permission_80)

    auth_permission_81 = Permission()
    auth_permission_81.name = u'Can delete practice'
    auth_permission_81.content_type = ContentType.objects.get(app_label="practices", model="practice")
    auth_permission_81.codename = u'delete_practice'
    auth_permission_81 = save_or_locate(auth_permission_81)

    auth_permission_82 = Permission()
    auth_permission_82.name = u'Can add practice contact'
    auth_permission_82.content_type = ContentType.objects.get(app_label="practices", model="practicecontact")
    auth_permission_82.codename = u'add_practicecontact'
    auth_permission_82 = save_or_locate(auth_permission_82)

    auth_permission_83 = Permission()
    auth_permission_83.name = u'Can change practice contact'
    auth_permission_83.content_type = ContentType.objects.get(app_label="practices", model="practicecontact")
    auth_permission_83.codename = u'change_practicecontact'
    auth_permission_83 = save_or_locate(auth_permission_83)

    auth_permission_84 = Permission()
    auth_permission_84.name = u'Can delete practice contact'
    auth_permission_84.content_type = ContentType.objects.get(app_label="practices", model="practicecontact")
    auth_permission_84.codename = u'delete_practicecontact'
    auth_permission_84 = save_or_locate(auth_permission_84)

    auth_permission_85 = Permission()
    auth_permission_85.name = u'Can add script'
    auth_permission_85.content_type = ContentType.objects.get(app_label="prescriptions", model="script")
    auth_permission_85.codename = u'add_script'
    auth_permission_85 = save_or_locate(auth_permission_85)

    auth_permission_86 = Permission()
    auth_permission_86.name = u'Can change script'
    auth_permission_86.content_type = ContentType.objects.get(app_label="prescriptions", model="script")
    auth_permission_86.codename = u'change_script'
    auth_permission_86 = save_or_locate(auth_permission_86)

    auth_permission_87 = Permission()
    auth_permission_87.name = u'Can delete script'
    auth_permission_87.content_type = ContentType.objects.get(app_label="prescriptions", model="script")
    auth_permission_87.codename = u'delete_script'
    auth_permission_87 = save_or_locate(auth_permission_87)

    auth_permission_88 = Permission()
    auth_permission_88.name = u'Can add script transaction'
    auth_permission_88.content_type = ContentType.objects.get(app_label="prescriptions", model="scripttransaction")
    auth_permission_88.codename = u'add_scripttransaction'
    auth_permission_88 = save_or_locate(auth_permission_88)

    auth_permission_89 = Permission()
    auth_permission_89.name = u'Can change script transaction'
    auth_permission_89.content_type = ContentType.objects.get(app_label="prescriptions", model="scripttransaction")
    auth_permission_89.codename = u'change_scripttransaction'
    auth_permission_89 = save_or_locate(auth_permission_89)

    auth_permission_90 = Permission()
    auth_permission_90.name = u'Can delete script transaction'
    auth_permission_90.content_type = ContentType.objects.get(app_label="prescriptions", model="scripttransaction")
    auth_permission_90.codename = u'delete_scripttransaction'
    auth_permission_90 = save_or_locate(auth_permission_90)

    auth_permission_91 = Permission()
    auth_permission_91.name = u'Can add region'
    auth_permission_91.content_type = ContentType.objects.get(app_label="regions", model="region")
    auth_permission_91.codename = u'add_region'
    auth_permission_91 = save_or_locate(auth_permission_91)

    auth_permission_92 = Permission()
    auth_permission_92.name = u'Can change region'
    auth_permission_92.content_type = ContentType.objects.get(app_label="regions", model="region")
    auth_permission_92.codename = u'change_region'
    auth_permission_92 = save_or_locate(auth_permission_92)

    auth_permission_93 = Permission()
    auth_permission_93.name = u'Can delete region'
    auth_permission_93.content_type = ContentType.objects.get(app_label="regions", model="region")
    auth_permission_93.codename = u'delete_region'
    auth_permission_93 = save_or_locate(auth_permission_93)

    auth_permission_94 = Permission()
    auth_permission_94.name = u'Can add sub region'
    auth_permission_94.content_type = ContentType.objects.get(app_label="regions", model="subregion")
    auth_permission_94.codename = u'add_subregion'
    auth_permission_94 = save_or_locate(auth_permission_94)

    auth_permission_95 = Permission()
    auth_permission_95.name = u'Can change sub region'
    auth_permission_95.content_type = ContentType.objects.get(app_label="regions", model="subregion")
    auth_permission_95.codename = u'change_subregion'
    auth_permission_95 = save_or_locate(auth_permission_95)

    auth_permission_96 = Permission()
    auth_permission_96.name = u'Can delete sub region'
    auth_permission_96.content_type = ContentType.objects.get(app_label="regions", model="subregion")
    auth_permission_96.codename = u'delete_subregion'
    auth_permission_96 = save_or_locate(auth_permission_96)

    auth_permission_97 = Permission()
    auth_permission_97.name = u'Can add commission tag'
    auth_permission_97.content_type = ContentType.objects.get(app_label="salesreps", model="commissiontag")
    auth_permission_97.codename = u'add_commissiontag'
    auth_permission_97 = save_or_locate(auth_permission_97)

    auth_permission_98 = Permission()
    auth_permission_98.name = u'Can change commission tag'
    auth_permission_98.content_type = ContentType.objects.get(app_label="salesreps", model="commissiontag")
    auth_permission_98.codename = u'change_commissiontag'
    auth_permission_98 = save_or_locate(auth_permission_98)

    auth_permission_99 = Permission()
    auth_permission_99.name = u'Can delete commission tag'
    auth_permission_99.content_type = ContentType.objects.get(app_label="salesreps", model="commissiontag")
    auth_permission_99.codename = u'delete_commissiontag'
    auth_permission_99 = save_or_locate(auth_permission_99)

    auth_permission_100 = Permission()
    auth_permission_100.name = u'Can add commission tag split'
    auth_permission_100.content_type = ContentType.objects.get(app_label="salesreps", model="commissiontagsplit")
    auth_permission_100.codename = u'add_commissiontagsplit'
    auth_permission_100 = save_or_locate(auth_permission_100)

    auth_permission_101 = Permission()
    auth_permission_101.name = u'Can change commission tag split'
    auth_permission_101.content_type = ContentType.objects.get(app_label="salesreps", model="commissiontagsplit")
    auth_permission_101.codename = u'change_commissiontagsplit'
    auth_permission_101 = save_or_locate(auth_permission_101)

    auth_permission_102 = Permission()
    auth_permission_102.name = u'Can delete commission tag split'
    auth_permission_102.content_type = ContentType.objects.get(app_label="salesreps", model="commissiontagsplit")
    auth_permission_102.codename = u'delete_commissiontagsplit'
    auth_permission_102 = save_or_locate(auth_permission_102)

    auth_permission_103 = Permission()
    auth_permission_103.name = u'Can add session'
    auth_permission_103.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_103.codename = u'add_session'
    auth_permission_103 = save_or_locate(auth_permission_103)

    auth_permission_104 = Permission()
    auth_permission_104.name = u'Can change session'
    auth_permission_104.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_104.codename = u'change_session'
    auth_permission_104 = save_or_locate(auth_permission_104)

    auth_permission_105 = Permission()
    auth_permission_105.name = u'Can delete session'
    auth_permission_105.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_105.codename = u'delete_session'
    auth_permission_105 = save_or_locate(auth_permission_105)

    auth_permission_106 = Permission()
    auth_permission_106.name = u'Can add site'
    auth_permission_106.content_type = ContentType.objects.get(app_label="sites", model="site")
    auth_permission_106.codename = u'add_site'
    auth_permission_106 = save_or_locate(auth_permission_106)

    auth_permission_107 = Permission()
    auth_permission_107.name = u'Can change site'
    auth_permission_107.content_type = ContentType.objects.get(app_label="sites", model="site")
    auth_permission_107.codename = u'change_site'
    auth_permission_107 = save_or_locate(auth_permission_107)

    auth_permission_108 = Permission()
    auth_permission_108.name = u'Can delete site'
    auth_permission_108.content_type = ContentType.objects.get(app_label="sites", model="site")
    auth_permission_108.codename = u'delete_site'
    auth_permission_108 = save_or_locate(auth_permission_108)

    auth_permission_109 = Permission()
    auth_permission_109.name = u'Can add category'
    auth_permission_109.content_type = ContentType.objects.get(app_label="tasks", model="category")
    auth_permission_109.codename = u'add_category'
    auth_permission_109 = save_or_locate(auth_permission_109)

    auth_permission_110 = Permission()
    auth_permission_110.name = u'Can change category'
    auth_permission_110.content_type = ContentType.objects.get(app_label="tasks", model="category")
    auth_permission_110.codename = u'change_category'
    auth_permission_110 = save_or_locate(auth_permission_110)

    auth_permission_111 = Permission()
    auth_permission_111.name = u'Can delete category'
    auth_permission_111.content_type = ContentType.objects.get(app_label="tasks", model="category")
    auth_permission_111.codename = u'delete_category'
    auth_permission_111 = save_or_locate(auth_permission_111)

    auth_permission_112 = Permission()
    auth_permission_112.name = u'Can add task'
    auth_permission_112.content_type = ContentType.objects.get(app_label="tasks", model="task")
    auth_permission_112.codename = u'add_task'
    auth_permission_112 = save_or_locate(auth_permission_112)

    auth_permission_113 = Permission()
    auth_permission_113.name = u'Can change task'
    auth_permission_113.content_type = ContentType.objects.get(app_label="tasks", model="task")
    auth_permission_113.codename = u'change_task'
    auth_permission_113 = save_or_locate(auth_permission_113)

    auth_permission_114 = Permission()
    auth_permission_114.name = u'Can delete task'
    auth_permission_114.content_type = ContentType.objects.get(app_label="tasks", model="task")
    auth_permission_114.codename = u'delete_task'
    auth_permission_114 = save_or_locate(auth_permission_114)

    #Processing model: Group

    from django.contrib.auth.models import Group

    auth_group_1 = Group()
    auth_group_1.name = u'AP Admin'
    auth_group_1 = save_or_locate(auth_group_1)

    auth_group_1.permissions.add(auth_permission_37)
    auth_group_1.permissions.add(auth_permission_38)
    auth_group_1.permissions.add(auth_permission_39)
    auth_group_1.permissions.add(auth_permission_40)
    auth_group_1.permissions.add(auth_permission_41)
    auth_group_1.permissions.add(auth_permission_42)
    auth_group_1.permissions.add(auth_permission_43)
    auth_group_1.permissions.add(auth_permission_44)
    auth_group_1.permissions.add(auth_permission_45)
    auth_group_1.permissions.add(auth_permission_55)
    auth_group_1.permissions.add(auth_permission_56)
    auth_group_1.permissions.add(auth_permission_57)
    auth_group_1.permissions.add(auth_permission_58)
    auth_group_1.permissions.add(auth_permission_59)
    auth_group_1.permissions.add(auth_permission_60)
    auth_group_1.permissions.add(auth_permission_61)
    auth_group_1.permissions.add(auth_permission_62)
    auth_group_1.permissions.add(auth_permission_63)
    auth_group_1.permissions.add(auth_permission_64)
    auth_group_1.permissions.add(auth_permission_65)
    auth_group_1.permissions.add(auth_permission_66)

    auth_group_2 = Group()
    auth_group_2.name = u'Posting'
    auth_group_2 = save_or_locate(auth_group_2)

    auth_group_2.permissions.add(auth_permission_55)
    auth_group_2.permissions.add(auth_permission_56)
    auth_group_2.permissions.add(auth_permission_57)
    auth_group_2.permissions.add(auth_permission_58)
    auth_group_2.permissions.add(auth_permission_59)
    auth_group_2.permissions.add(auth_permission_60)
    auth_group_2.permissions.add(auth_permission_61)
    auth_group_2.permissions.add(auth_permission_62)
    auth_group_2.permissions.add(auth_permission_63)

    auth_group_3 = Group()
    auth_group_3.name = u'Rep Admin'
    auth_group_3 = save_or_locate(auth_group_3)

    auth_group_4 = Group()
    auth_group_4.name = u'Sales Rep'
    auth_group_4 = save_or_locate(auth_group_4)

    auth_group_4.permissions.add(auth_permission_4)
    auth_group_4.permissions.add(auth_permission_5)
    auth_group_4.permissions.add(auth_permission_6)
    auth_group_4.permissions.add(auth_permission_13)
    auth_group_4.permissions.add(auth_permission_14)
    auth_group_4.permissions.add(auth_permission_15)
    auth_group_4.permissions.add(auth_permission_19)
    auth_group_4.permissions.add(auth_permission_20)
    auth_group_4.permissions.add(auth_permission_21)
    auth_group_4.permissions.add(auth_permission_22)
    auth_group_4.permissions.add(auth_permission_23)
    auth_group_4.permissions.add(auth_permission_24)
    auth_group_4.permissions.add(auth_permission_25)
    auth_group_4.permissions.add(auth_permission_26)
    auth_group_4.permissions.add(auth_permission_27)
    auth_group_4.permissions.add(auth_permission_28)
    auth_group_4.permissions.add(auth_permission_29)
    auth_group_4.permissions.add(auth_permission_30)
    auth_group_4.permissions.add(auth_permission_31)
    auth_group_4.permissions.add(auth_permission_32)
    auth_group_4.permissions.add(auth_permission_33)
    auth_group_4.permissions.add(auth_permission_34)
    auth_group_4.permissions.add(auth_permission_35)
    auth_group_4.permissions.add(auth_permission_36)
    auth_group_4.permissions.add(auth_permission_67)
    auth_group_4.permissions.add(auth_permission_68)
    auth_group_4.permissions.add(auth_permission_69)
    auth_group_4.permissions.add(auth_permission_70)
    auth_group_4.permissions.add(auth_permission_71)
    auth_group_4.permissions.add(auth_permission_72)
    auth_group_4.permissions.add(auth_permission_73)
    auth_group_4.permissions.add(auth_permission_74)
    auth_group_4.permissions.add(auth_permission_75)
    auth_group_4.permissions.add(auth_permission_76)
    auth_group_4.permissions.add(auth_permission_77)
    auth_group_4.permissions.add(auth_permission_78)
    auth_group_4.permissions.add(auth_permission_79)
    auth_group_4.permissions.add(auth_permission_80)
    auth_group_4.permissions.add(auth_permission_81)
    auth_group_4.permissions.add(auth_permission_82)
    auth_group_4.permissions.add(auth_permission_83)
    auth_group_4.permissions.add(auth_permission_84)
    auth_group_4.permissions.add(auth_permission_91)
    auth_group_4.permissions.add(auth_permission_92)
    auth_group_4.permissions.add(auth_permission_93)
    auth_group_4.permissions.add(auth_permission_94)
    auth_group_4.permissions.add(auth_permission_95)
    auth_group_4.permissions.add(auth_permission_96)
    auth_group_4.permissions.add(auth_permission_97)
    auth_group_4.permissions.add(auth_permission_98)
    auth_group_4.permissions.add(auth_permission_99)
    auth_group_4.permissions.add(auth_permission_100)
    auth_group_4.permissions.add(auth_permission_101)
    auth_group_4.permissions.add(auth_permission_102)
    auth_group_4.permissions.add(auth_permission_109)
    auth_group_4.permissions.add(auth_permission_110)
    auth_group_4.permissions.add(auth_permission_111)
    auth_group_4.permissions.add(auth_permission_112)
    auth_group_4.permissions.add(auth_permission_113)
    auth_group_4.permissions.add(auth_permission_114)

    #Processing model: User

    from django.contrib.auth.models import User

    auth_user_1 = User()
    auth_user_1.password = u'pbkdf2_sha256$10000$CsrwThaPvK4E$zqsORsqXeke6GmIufQAnICQcg54iDdEBX20aQj4yDoo='
    auth_user_1.last_login = datetime.datetime(2013, 6, 26, 19, 13, 38, tzinfo=<UTC>)
    auth_user_1.is_superuser = True
    auth_user_1.username = u'ccohen'
    auth_user_1.first_name = u'Craig'
    auth_user_1.last_name = u'Cohen'
    auth_user_1.email = u'chc5286@gmail.com'
    auth_user_1.is_staff = True
    auth_user_1.is_active = True
    auth_user_1.date_joined = datetime.datetime(2013, 6, 7, 0, 33, 38, tzinfo=<UTC>)
    auth_user_1 = save_or_locate(auth_user_1)

    auth_user_1.groups.add(auth_group_3)

    auth_user_2 = User()
    auth_user_2.password = u'pbkdf2_sha256$10000$R5lPYefXw630$+2k7vtEL0XaCMaH70M+1C/8OFFImh95b68YwrBuimkc='
    auth_user_2.last_login = datetime.datetime(2013, 6, 11, 15, 22, 28, tzinfo=<UTC>)
    auth_user_2.is_superuser = False
    auth_user_2.username = u'mschmier'
    auth_user_2.first_name = u'Mark'
    auth_user_2.last_name = u'Schmier'
    auth_user_2.email = u'mschmier@optonline.net'
    auth_user_2.is_staff = True
    auth_user_2.is_active = True
    auth_user_2.date_joined = datetime.datetime(2013, 6, 11, 15, 22, 28, tzinfo=<UTC>)
    auth_user_2 = save_or_locate(auth_user_2)

    auth_user_2.groups.add(auth_group_1)

    auth_user_3 = User()
    auth_user_3.password = u'pbkdf2_sha256$10000$ezAlzSAWDo9M$RUmR/sDnD2Dvm+1VhO9hHG0doysphj2A6BDVSoFQd64='
    auth_user_3.last_login = datetime.datetime(2013, 6, 26, 4, 6, 44, tzinfo=<UTC>)
    auth_user_3.is_superuser = False
    auth_user_3.username = u'bbloom'
    auth_user_3.first_name = u'Bryan'
    auth_user_3.last_name = u'Bloom'
    auth_user_3.email = u'bebloom@gmail.com'
    auth_user_3.is_staff = True
    auth_user_3.is_active = True
    auth_user_3.date_joined = datetime.datetime(2013, 6, 11, 15, 23, 14, tzinfo=<UTC>)
    auth_user_3 = save_or_locate(auth_user_3)

    auth_user_3.groups.add(auth_group_4)
    auth_user_3.groups.add(auth_group_3)

    auth_user_4 = User()
    auth_user_4.password = u'pbkdf2_sha256$10000$ncOskosj145z$XQirLTTzh5iPG7io0iUYgsClNKe+qMq9Qktv+OxqEDQ='
    auth_user_4.last_login = datetime.datetime(2013, 6, 14, 18, 40, 4, tzinfo=<UTC>)
    auth_user_4.is_superuser = False
    auth_user_4.username = u'gbortnick'
    auth_user_4.first_name = u'Glenn'
    auth_user_4.last_name = u'Bortnick'
    auth_user_4.email = u'glennb@lindencare.com'
    auth_user_4.is_staff = True
    auth_user_4.is_active = True
    auth_user_4.date_joined = datetime.datetime(2013, 6, 11, 15, 24, 3, tzinfo=<UTC>)
    auth_user_4 = save_or_locate(auth_user_4)

    auth_user_4.groups.add(auth_group_4)
    auth_user_4.groups.add(auth_group_3)

    auth_user_5 = User()
    auth_user_5.password = u'pbkdf2_sha256$10000$2NTlpEiCXozP$tuwQesH9qHhh/bTazHEM0WmJHD/W3aHykK22iCUFhdI='
    auth_user_5.last_login = datetime.datetime(2013, 6, 11, 15, 25, 5, tzinfo=<UTC>)
    auth_user_5.is_superuser = False
    auth_user_5.username = u'cleibowitz'
    auth_user_5.first_name = u'Choy'
    auth_user_5.last_name = u'Leibowitz'
    auth_user_5.email = u'cleibowitz@lindencare.com'
    auth_user_5.is_staff = True
    auth_user_5.is_active = True
    auth_user_5.date_joined = datetime.datetime(2013, 6, 11, 15, 25, 5, tzinfo=<UTC>)
    auth_user_5 = save_or_locate(auth_user_5)

    auth_user_5.groups.add(auth_group_2)

    auth_user_6 = User()
    auth_user_6.password = u'pbkdf2_sha256$10000$7iK6Bfcl25CP$88uwcTCjz6A15ak8/Mlb9/AwM16lTfyeTT2BFWrvKhk='
    auth_user_6.last_login = datetime.datetime(2013, 6, 26, 4, 7, 8, tzinfo=<UTC>)
    auth_user_6.is_superuser = False
    auth_user_6.username = u'pblock'
    auth_user_6.first_name = u'Paul'
    auth_user_6.last_name = u'Block'
    auth_user_6.email = u''
    auth_user_6.is_staff = True
    auth_user_6.is_active = True
    auth_user_6.date_joined = datetime.datetime(2013, 6, 14, 4, 33, 38, tzinfo=<UTC>)
    auth_user_6 = save_or_locate(auth_user_6)

    auth_user_6.groups.add(auth_group_4)

    #Processing model: Session

    from django.contrib.sessions.models import Session

    django_session_1 = Session()
    django_session_1.session_key = u'2t71lqcde4nwhtglg5nqy4pvq6xbnqoo'
    django_session_1.session_data = u'ZWFmYTY5ZWRiYTk3Y2Q3YzhkOGNjMDIyYjAxM2Y2MGJhZjY1OTFjODqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLAXUu'
    django_session_1.expire_date = datetime.datetime(2013, 7, 10, 19, 13, 38, tzinfo=<UTC>)
    django_session_1 = save_or_locate(django_session_1)

    django_session_2 = Session()
    django_session_2.session_key = u'2z48h7ed8dvix1qbdx5paswhdhb1xnat'
    django_session_2.session_data = u'NjZlYzM1N2UxODJlZDEyZDc1Y2Q1MTA1NTkxNzBkNzc4NWFmMzUzYjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLBHUu'
    django_session_2.expire_date = datetime.datetime(2013, 6, 28, 4, 38, 11, tzinfo=<UTC>)
    django_session_2 = save_or_locate(django_session_2)

    django_session_3 = Session()
    django_session_3.session_key = u'8piwop27duwm1ucm6q5anhuef1nbll7w'
    django_session_3.session_data = u'MjQyMzRiNWQzZGM2ZGUzYzc4Mjg2NGMwOWUwZWFjMDc0ZWEyZjI1NzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLBnUu'
    django_session_3.expire_date = datetime.datetime(2013, 7, 10, 4, 7, 8, tzinfo=<UTC>)
    django_session_3 = save_or_locate(django_session_3)

    django_session_4 = Session()
    django_session_4.session_key = u'bl70ewss5rdtpkxg3yedyzly3g6rs36j'
    django_session_4.session_data = u'ZWFmYTY5ZWRiYTk3Y2Q3YzhkOGNjMDIyYjAxM2Y2MGJhZjY1OTFjODqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLAXUu'
    django_session_4.expire_date = datetime.datetime(2013, 6, 28, 13, 29, 52, tzinfo=<UTC>)
    django_session_4 = save_or_locate(django_session_4)

    django_session_5 = Session()
    django_session_5.session_key = u'bmcwjmsux6wv14zxlnm2r39rd2g4y4zy'
    django_session_5.session_data = u'NjZlYzM1N2UxODJlZDEyZDc1Y2Q1MTA1NTkxNzBkNzc4NWFmMzUzYjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLBHUu'
    django_session_5.expire_date = datetime.datetime(2013, 6, 25, 16, 31, 18, tzinfo=<UTC>)
    django_session_5 = save_or_locate(django_session_5)

    django_session_6 = Session()
    django_session_6.session_key = u'cz79s5tdulimyvafmy7kkc1g8qugyrcn'
    django_session_6.session_data = u'NjZlYzM1N2UxODJlZDEyZDc1Y2Q1MTA1NTkxNzBkNzc4NWFmMzUzYjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLBHUu'
    django_session_6.expire_date = datetime.datetime(2013, 6, 28, 18, 40, 4, tzinfo=<UTC>)
    django_session_6 = save_or_locate(django_session_6)

    django_session_7 = Session()
    django_session_7.session_key = u'gke4p1wsx7wgsbkhy2jkqoc1kidphg6j'
    django_session_7.session_data = u'ZWFmYTY5ZWRiYTk3Y2Q3YzhkOGNjMDIyYjAxM2Y2MGJhZjY1OTFjODqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLAXUu'
    django_session_7.expire_date = datetime.datetime(2013, 7, 1, 19, 49, 57, tzinfo=<UTC>)
    django_session_7 = save_or_locate(django_session_7)

    django_session_8 = Session()
    django_session_8.session_key = u'grkhan1b7q8h8n90paj5kbihpg0o3v46'
    django_session_8.session_data = u'ZWFmYTY5ZWRiYTk3Y2Q3YzhkOGNjMDIyYjAxM2Y2MGJhZjY1OTFjODqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLAXUu'
    django_session_8.expire_date = datetime.datetime(2013, 6, 27, 16, 44, 19, tzinfo=<UTC>)
    django_session_8 = save_or_locate(django_session_8)

    django_session_9 = Session()
    django_session_9.session_key = u'pk543uxqfxu379n8ml29l33lyma8np9z'
    django_session_9.session_data = u'ZWFmYTY5ZWRiYTk3Y2Q3YzhkOGNjMDIyYjAxM2Y2MGJhZjY1OTFjODqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLAXUu'
    django_session_9.expire_date = datetime.datetime(2013, 6, 28, 11, 48, 5, tzinfo=<UTC>)
    django_session_9 = save_or_locate(django_session_9)

    django_session_10 = Session()
    django_session_10.session_key = u's59cyrs4pwne9z87wxu333q5u8sjq2c6'
    django_session_10.session_data = u'ZWFmYTY5ZWRiYTk3Y2Q3YzhkOGNjMDIyYjAxM2Y2MGJhZjY1OTFjODqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLAXUu'
    django_session_10.expire_date = datetime.datetime(2013, 7, 3, 17, 24, 4, tzinfo=<UTC>)
    django_session_10 = save_or_locate(django_session_10)

    django_session_11 = Session()
    django_session_11.session_key = u'scn1zlizm38v08rjxue2hgw4vy27n4k2'
    django_session_11.session_data = u'ZWFmYTY5ZWRiYTk3Y2Q3YzhkOGNjMDIyYjAxM2Y2MGJhZjY1OTFjODqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLAXUu'
    django_session_11.expire_date = datetime.datetime(2013, 7, 1, 18, 1, 19, tzinfo=<UTC>)
    django_session_11 = save_or_locate(django_session_11)

    django_session_12 = Session()
    django_session_12.session_key = u'thshrh9ooo7hou0623el4ngopkatptoe'
    django_session_12.session_data = u'ZWFmYTY5ZWRiYTk3Y2Q3YzhkOGNjMDIyYjAxM2Y2MGJhZjY1OTFjODqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLAXUu'
    django_session_12.expire_date = datetime.datetime(2013, 7, 2, 15, 1, 5, tzinfo=<UTC>)
    django_session_12 = save_or_locate(django_session_12)

    django_session_13 = Session()
    django_session_13.session_key = u'x5uy9b0fj4tpma8zmokiniquzj2029n1'
    django_session_13.session_data = u'ZWFmYTY5ZWRiYTk3Y2Q3YzhkOGNjMDIyYjAxM2Y2MGJhZjY1OTFjODqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLAXUu'
    django_session_13.expire_date = datetime.datetime(2013, 6, 25, 21, 19, 57, tzinfo=<UTC>)
    django_session_13 = save_or_locate(django_session_13)

    #Processing model: Site

    from django.contrib.sites.models import Site

    django_site_1 = Site()
    django_site_1.domain = u'example.com'
    django_site_1.name = u'example.com'
    django_site_1 = save_or_locate(django_site_1)

    #Processing model: LogEntry

    from django.contrib.admin.models import LogEntry

    django_admin_log_1 = LogEntry()
    django_admin_log_1.action_time = datetime.datetime(2013, 6, 26, 4, 5, 55, tzinfo=<UTC>)
    django_admin_log_1.user = auth_user_1
    django_admin_log_1.content_type = ContentType.objects.get(app_label="tasks", model="task")
    django_admin_log_1.object_id = u'3'
    django_admin_log_1.object_repr = u'Call Fentora Rep'
    django_admin_log_1.action_flag = 1
    django_admin_log_1.change_message = u''
    django_admin_log_1 = save_or_locate(django_admin_log_1)

    django_admin_log_2 = LogEntry()
    django_admin_log_2.action_time = datetime.datetime(2013, 6, 26, 4, 5, 24, tzinfo=<UTC>)
    django_admin_log_2.user = auth_user_1
    django_admin_log_2.content_type = ContentType.objects.get(app_label="tasks", model="task")
    django_admin_log_2.object_id = u'2'
    django_admin_log_2.object_repr = u'Script 380222'
    django_admin_log_2.action_flag = 1
    django_admin_log_2.change_message = u''
    django_admin_log_2 = save_or_locate(django_admin_log_2)

    django_admin_log_3 = LogEntry()
    django_admin_log_3.action_time = datetime.datetime(2013, 6, 26, 4, 4, 50, tzinfo=<UTC>)
    django_admin_log_3.user = auth_user_1
    django_admin_log_3.content_type = ContentType.objects.get(app_label="tasks", model="task")
    django_admin_log_3.object_id = u'1'
    django_admin_log_3.object_repr = u'Go to bank'
    django_admin_log_3.action_flag = 1
    django_admin_log_3.change_message = u''
    django_admin_log_3 = save_or_locate(django_admin_log_3)

    django_admin_log_4 = LogEntry()
    django_admin_log_4.action_time = datetime.datetime(2013, 6, 26, 4, 4, 24, tzinfo=<UTC>)
    django_admin_log_4.user = auth_user_1
    django_admin_log_4.content_type = ContentType.objects.get(app_label="tasks", model="category")
    django_admin_log_4.object_id = u'5'
    django_admin_log_4.object_repr = u'Refills'
    django_admin_log_4.action_flag = 1
    django_admin_log_4.change_message = u''
    django_admin_log_4 = save_or_locate(django_admin_log_4)

    django_admin_log_5 = LogEntry()
    django_admin_log_5.action_time = datetime.datetime(2013, 6, 26, 4, 4, 17, tzinfo=<UTC>)
    django_admin_log_5.user = auth_user_1
    django_admin_log_5.content_type = ContentType.objects.get(app_label="tasks", model="category")
    django_admin_log_5.object_id = u'4'
    django_admin_log_5.object_repr = u'At Home'
    django_admin_log_5.action_flag = 1
    django_admin_log_5.change_message = u''
    django_admin_log_5 = save_or_locate(django_admin_log_5)

    django_admin_log_6 = LogEntry()
    django_admin_log_6.action_time = datetime.datetime(2013, 6, 26, 4, 4, 9, tzinfo=<UTC>)
    django_admin_log_6.user = auth_user_1
    django_admin_log_6.content_type = ContentType.objects.get(app_label="tasks", model="category")
    django_admin_log_6.object_id = u'3'
    django_admin_log_6.object_repr = u'In Pharmacy'
    django_admin_log_6.action_flag = 1
    django_admin_log_6.change_message = u''
    django_admin_log_6 = save_or_locate(django_admin_log_6)

    django_admin_log_7 = LogEntry()
    django_admin_log_7.action_time = datetime.datetime(2013, 6, 26, 4, 4, 2, tzinfo=<UTC>)
    django_admin_log_7.user = auth_user_1
    django_admin_log_7.content_type = ContentType.objects.get(app_label="tasks", model="category")
    django_admin_log_7.object_id = u'2'
    django_admin_log_7.object_repr = u'Text Message'
    django_admin_log_7.action_flag = 1
    django_admin_log_7.change_message = u''
    django_admin_log_7 = save_or_locate(django_admin_log_7)

    django_admin_log_8 = LogEntry()
    django_admin_log_8.action_time = datetime.datetime(2013, 6, 26, 4, 3, 52, tzinfo=<UTC>)
    django_admin_log_8.user = auth_user_1
    django_admin_log_8.content_type = ContentType.objects.get(app_label="tasks", model="category")
    django_admin_log_8.object_id = u'1'
    django_admin_log_8.object_repr = u'Phone Call'
    django_admin_log_8.action_flag = 1
    django_admin_log_8.change_message = u''
    django_admin_log_8 = save_or_locate(django_admin_log_8)

    django_admin_log_9 = LogEntry()
    django_admin_log_9.action_time = datetime.datetime(2013, 6, 26, 4, 2, 55, tzinfo=<UTC>)
    django_admin_log_9.user = auth_user_1
    django_admin_log_9.content_type = ContentType.objects.get(app_label="payments", model="paymenttransaction")
    django_admin_log_9.object_id = u'3'
    django_admin_log_9.object_repr = u'3457.32'
    django_admin_log_9.action_flag = 1
    django_admin_log_9.change_message = u''
    django_admin_log_9 = save_or_locate(django_admin_log_9)

    django_admin_log_10 = LogEntry()
    django_admin_log_10.action_time = datetime.datetime(2013, 6, 26, 4, 2, 35, tzinfo=<UTC>)
    django_admin_log_10.user = auth_user_1
    django_admin_log_10.content_type = ContentType.objects.get(app_label="payments", model="paymenttransaction")
    django_admin_log_10.object_id = u'2'
    django_admin_log_10.object_repr = u'657.33'
    django_admin_log_10.action_flag = 1
    django_admin_log_10.change_message = u''
    django_admin_log_10 = save_or_locate(django_admin_log_10)

    django_admin_log_11 = LogEntry()
    django_admin_log_11.action_time = datetime.datetime(2013, 6, 26, 3, 59, 9, tzinfo=<UTC>)
    django_admin_log_11.user = auth_user_1
    django_admin_log_11.content_type = ContentType.objects.get(app_label="prescriptions", model="scripttransaction")
    django_admin_log_11.object_id = u'4'
    django_admin_log_11.object_repr = u'341.56'
    django_admin_log_11.action_flag = 1
    django_admin_log_11.change_message = u''
    django_admin_log_11 = save_or_locate(django_admin_log_11)

    django_admin_log_12 = LogEntry()
    django_admin_log_12.action_time = datetime.datetime(2013, 6, 26, 3, 58, 50, tzinfo=<UTC>)
    django_admin_log_12.user = auth_user_1
    django_admin_log_12.content_type = ContentType.objects.get(app_label="prescriptions", model="scripttransaction")
    django_admin_log_12.object_id = u'3'
    django_admin_log_12.object_repr = u'3457.32'
    django_admin_log_12.action_flag = 1
    django_admin_log_12.change_message = u''
    django_admin_log_12 = save_or_locate(django_admin_log_12)

    django_admin_log_13 = LogEntry()
    django_admin_log_13.action_time = datetime.datetime(2013, 6, 26, 3, 58, 27, tzinfo=<UTC>)
    django_admin_log_13.user = auth_user_1
    django_admin_log_13.content_type = ContentType.objects.get(app_label="prescriptions", model="scripttransaction")
    django_admin_log_13.object_id = u'2'
    django_admin_log_13.object_repr = u'657.33'
    django_admin_log_13.action_flag = 1
    django_admin_log_13.change_message = u''
    django_admin_log_13 = save_or_locate(django_admin_log_13)

    django_admin_log_14 = LogEntry()
    django_admin_log_14.action_time = datetime.datetime(2013, 6, 26, 3, 56, 25, tzinfo=<UTC>)
    django_admin_log_14.user = auth_user_1
    django_admin_log_14.content_type = ContentType.objects.get(app_label="prescriptions", model="script")
    django_admin_log_14.object_id = u'2'
    django_admin_log_14.object_repr = u'345322 1'
    django_admin_log_14.action_flag = 1
    django_admin_log_14.change_message = u''
    django_admin_log_14 = save_or_locate(django_admin_log_14)

    django_admin_log_15 = LogEntry()
    django_admin_log_15.action_time = datetime.datetime(2013, 6, 26, 3, 55, 32, tzinfo=<UTC>)
    django_admin_log_15.user = auth_user_1
    django_admin_log_15.content_type = ContentType.objects.get(app_label="prescriptions", model="script")
    django_admin_log_15.object_id = u'1'
    django_admin_log_15.object_repr = u'425333 0'
    django_admin_log_15.action_flag = 1
    django_admin_log_15.change_message = u''
    django_admin_log_15 = save_or_locate(django_admin_log_15)

    django_admin_log_16 = LogEntry()
    django_admin_log_16.action_time = datetime.datetime(2013, 6, 26, 3, 53, 2, tzinfo=<UTC>)
    django_admin_log_16.user = auth_user_1
    django_admin_log_16.content_type = ContentType.objects.get(app_label="practices", model="multipractice")
    django_admin_log_16.object_id = u'2'
    django_admin_log_16.object_repr = u'Upper East Pain'
    django_admin_log_16.action_flag = 1
    django_admin_log_16.change_message = u''
    django_admin_log_16 = save_or_locate(django_admin_log_16)

    django_admin_log_17 = LogEntry()
    django_admin_log_17.action_time = datetime.datetime(2013, 6, 26, 3, 52, 32, tzinfo=<UTC>)
    django_admin_log_17.user = auth_user_1
    django_admin_log_17.content_type = ContentType.objects.get(app_label="practices", model="practicecontact")
    django_admin_log_17.object_id = u'3'
    django_admin_log_17.object_repr = u'Jill Marx'
    django_admin_log_17.action_flag = 1
    django_admin_log_17.change_message = u''
    django_admin_log_17 = save_or_locate(django_admin_log_17)

    django_admin_log_18 = LogEntry()
    django_admin_log_18.action_time = datetime.datetime(2013, 6, 26, 3, 49, 44, tzinfo=<UTC>)
    django_admin_log_18.user = auth_user_1
    django_admin_log_18.content_type = ContentType.objects.get(app_label="practices", model="doctor")
    django_admin_log_18.object_id = u'6'
    django_admin_log_18.object_repr = u'Dr. Lebron James'
    django_admin_log_18.action_flag = 1
    django_admin_log_18.change_message = u''
    django_admin_log_18 = save_or_locate(django_admin_log_18)

    django_admin_log_19 = LogEntry()
    django_admin_log_19.action_time = datetime.datetime(2013, 6, 26, 3, 49, 39, tzinfo=<UTC>)
    django_admin_log_19.user = auth_user_1
    django_admin_log_19.content_type = ContentType.objects.get(app_label="practices", model="practice")
    django_admin_log_19.object_id = u'6'
    django_admin_log_19.object_repr = u'Douglas Schwartz West'
    django_admin_log_19.action_flag = 1
    django_admin_log_19.change_message = u''
    django_admin_log_19 = save_or_locate(django_admin_log_19)

    django_admin_log_20 = LogEntry()
    django_admin_log_20.action_time = datetime.datetime(2013, 6, 26, 3, 48, 46, tzinfo=<UTC>)
    django_admin_log_20.user = auth_user_1
    django_admin_log_20.content_type = ContentType.objects.get(app_label="practices", model="doctor")
    django_admin_log_20.object_id = u'5'
    django_admin_log_20.object_repr = u'Dr. John Doe'
    django_admin_log_20.action_flag = 1
    django_admin_log_20.change_message = u''
    django_admin_log_20 = save_or_locate(django_admin_log_20)

    django_admin_log_21 = LogEntry()
    django_admin_log_21.action_time = datetime.datetime(2013, 6, 26, 3, 47, 56, tzinfo=<UTC>)
    django_admin_log_21.user = auth_user_1
    django_admin_log_21.content_type = ContentType.objects.get(app_label="practices", model="doctor")
    django_admin_log_21.object_id = u'2'
    django_admin_log_21.object_repr = u'Dr. Douglas Schwartz'
    django_admin_log_21.action_flag = 1
    django_admin_log_21.change_message = u''
    django_admin_log_21 = save_or_locate(django_admin_log_21)

    django_admin_log_22 = LogEntry()
    django_admin_log_22.action_time = datetime.datetime(2013, 6, 26, 3, 46, 30, tzinfo=<UTC>)
    django_admin_log_22.user = auth_user_1
    django_admin_log_22.content_type = ContentType.objects.get(app_label="practices", model="practice")
    django_admin_log_22.object_id = u'5'
    django_admin_log_22.object_repr = u'Douglas Schwartz East'
    django_admin_log_22.action_flag = 1
    django_admin_log_22.change_message = u''
    django_admin_log_22 = save_or_locate(django_admin_log_22)

    django_admin_log_23 = LogEntry()
    django_admin_log_23.action_time = datetime.datetime(2013, 6, 26, 3, 45, 21, tzinfo=<UTC>)
    django_admin_log_23.user = auth_user_1
    django_admin_log_23.content_type = ContentType.objects.get(app_label="practices", model="multipractice")
    django_admin_log_23.object_id = u'1'
    django_admin_log_23.object_repr = u'Schwartz Incorporated'
    django_admin_log_23.action_flag = 1
    django_admin_log_23.change_message = u''
    django_admin_log_23 = save_or_locate(django_admin_log_23)

    django_admin_log_24 = LogEntry()
    django_admin_log_24.action_time = datetime.datetime(2013, 6, 26, 3, 43, 33, tzinfo=<UTC>)
    django_admin_log_24.user = auth_user_1
    django_admin_log_24.content_type = ContentType.objects.get(app_label="payments", model="check")
    django_admin_log_24.object_id = u'2'
    django_admin_log_24.object_repr = u'46744673'
    django_admin_log_24.action_flag = 1
    django_admin_log_24.change_message = u''
    django_admin_log_24 = save_or_locate(django_admin_log_24)

    django_admin_log_25 = LogEntry()
    django_admin_log_25.action_time = datetime.datetime(2013, 6, 26, 3, 42, 58, tzinfo=<UTC>)
    django_admin_log_25.user = auth_user_1
    django_admin_log_25.content_type = ContentType.objects.get(app_label="payments", model="check")
    django_admin_log_25.object_id = u'1'
    django_admin_log_25.object_repr = u'000523452'
    django_admin_log_25.action_flag = 1
    django_admin_log_25.change_message = u''
    django_admin_log_25 = save_or_locate(django_admin_log_25)

    django_admin_log_26 = LogEntry()
    django_admin_log_26.action_time = datetime.datetime(2013, 6, 26, 3, 42, 7, tzinfo=<UTC>)
    django_admin_log_26.user = auth_user_1
    django_admin_log_26.content_type = ContentType.objects.get(app_label="payments", model="batch")
    django_admin_log_26.object_id = u'2'
    django_admin_log_26.object_repr = u'062313A'
    django_admin_log_26.action_flag = 1
    django_admin_log_26.change_message = u''
    django_admin_log_26 = save_or_locate(django_admin_log_26)

    django_admin_log_27 = LogEntry()
    django_admin_log_27.action_time = datetime.datetime(2013, 6, 26, 3, 41, 38, tzinfo=<UTC>)
    django_admin_log_27.user = auth_user_1
    django_admin_log_27.content_type = ContentType.objects.get(app_label="payments", model="batch")
    django_admin_log_27.object_id = u'1'
    django_admin_log_27.object_repr = u'062513A'
    django_admin_log_27.action_flag = 1
    django_admin_log_27.change_message = u''
    django_admin_log_27 = save_or_locate(django_admin_log_27)

    django_admin_log_28 = LogEntry()
    django_admin_log_28.action_time = datetime.datetime(2013, 6, 26, 3, 39, 49, tzinfo=<UTC>)
    django_admin_log_28.user = auth_user_1
    django_admin_log_28.content_type = ContentType.objects.get(app_label="patients", model="patient")
    django_admin_log_28.object_id = u'3'
    django_admin_log_28.object_repr = u'Monica Samuel'
    django_admin_log_28.action_flag = 1
    django_admin_log_28.change_message = u''
    django_admin_log_28 = save_or_locate(django_admin_log_28)

    django_admin_log_29 = LogEntry()
    django_admin_log_29.action_time = datetime.datetime(2013, 6, 26, 3, 39, 40, tzinfo=<UTC>)
    django_admin_log_29.user = auth_user_1
    django_admin_log_29.content_type = ContentType.objects.get(app_label="patients", model="patient")
    django_admin_log_29.object_id = u'2'
    django_admin_log_29.object_repr = u'Scott Meltzer'
    django_admin_log_29.action_flag = 1
    django_admin_log_29.change_message = u''
    django_admin_log_29 = save_or_locate(django_admin_log_29)

    django_admin_log_30 = LogEntry()
    django_admin_log_30.action_time = datetime.datetime(2013, 6, 26, 3, 39, 20, tzinfo=<UTC>)
    django_admin_log_30.user = auth_user_1
    django_admin_log_30.content_type = ContentType.objects.get(app_label="patients", model="patient")
    django_admin_log_30.object_id = u'1'
    django_admin_log_30.object_repr = u'Craig Cohen'
    django_admin_log_30.action_flag = 1
    django_admin_log_30.change_message = u''
    django_admin_log_30 = save_or_locate(django_admin_log_30)

    django_admin_log_31 = LogEntry()
    django_admin_log_31.action_time = datetime.datetime(2013, 6, 26, 3, 37, 38, tzinfo=<UTC>)
    django_admin_log_31.user = auth_user_1
    django_admin_log_31.content_type = ContentType.objects.get(app_label="insurance", model="insuror")
    django_admin_log_31.object_id = u'3'
    django_admin_log_31.object_repr = u'AL '
    django_admin_log_31.action_flag = 1
    django_admin_log_31.change_message = u''
    django_admin_log_31 = save_or_locate(django_admin_log_31)

    django_admin_log_32 = LogEntry()
    django_admin_log_32.action_time = datetime.datetime(2013, 6, 26, 3, 37, 33, tzinfo=<UTC>)
    django_admin_log_32.user = auth_user_1
    django_admin_log_32.content_type = ContentType.objects.get(app_label="insurance", model="binnumber")
    django_admin_log_32.object_id = u'7'
    django_admin_log_32.object_repr = u'BinNumber object'
    django_admin_log_32.action_flag = 1
    django_admin_log_32.change_message = u''
    django_admin_log_32 = save_or_locate(django_admin_log_32)

    django_admin_log_33 = LogEntry()
    django_admin_log_33.action_time = datetime.datetime(2013, 6, 26, 3, 32, 31, tzinfo=<UTC>)
    django_admin_log_33.user = auth_user_1
    django_admin_log_33.content_type = ContentType.objects.get(app_label="insurance", model="insuror")
    django_admin_log_33.object_id = u'2'
    django_admin_log_33.object_repr = u'MC J9999'
    django_admin_log_33.action_flag = 1
    django_admin_log_33.change_message = u''
    django_admin_log_33 = save_or_locate(django_admin_log_33)

    django_admin_log_34 = LogEntry()
    django_admin_log_34.action_time = datetime.datetime(2013, 6, 26, 3, 31, 11, tzinfo=<UTC>)
    django_admin_log_34.user = auth_user_1
    django_admin_log_34.content_type = ContentType.objects.get(app_label="insurance", model="insuror")
    django_admin_log_34.object_id = u'1'
    django_admin_log_34.object_repr = u'PD '
    django_admin_log_34.action_flag = 1
    django_admin_log_34.change_message = u''
    django_admin_log_34 = save_or_locate(django_admin_log_34)

    django_admin_log_35 = LogEntry()
    django_admin_log_35.action_time = datetime.datetime(2013, 6, 26, 3, 30, 32, tzinfo=<UTC>)
    django_admin_log_35.user = auth_user_1
    django_admin_log_35.content_type = ContentType.objects.get(app_label="insurance", model="binnumber")
    django_admin_log_35.object_id = u'4'
    django_admin_log_35.object_repr = u'BinNumber object'
    django_admin_log_35.action_flag = 1
    django_admin_log_35.change_message = u''
    django_admin_log_35 = save_or_locate(django_admin_log_35)

    django_admin_log_36 = LogEntry()
    django_admin_log_36.action_time = datetime.datetime(2013, 6, 26, 3, 27, 24, tzinfo=<UTC>)
    django_admin_log_36.user = auth_user_1
    django_admin_log_36.content_type = ContentType.objects.get(app_label="insurance", model="payor")
    django_admin_log_36.object_id = u'3'
    django_admin_log_36.object_repr = u'Express Scripts'
    django_admin_log_36.action_flag = 1
    django_admin_log_36.change_message = u''
    django_admin_log_36 = save_or_locate(django_admin_log_36)

    django_admin_log_37 = LogEntry()
    django_admin_log_37.action_time = datetime.datetime(2013, 6, 26, 3, 27, 16, tzinfo=<UTC>)
    django_admin_log_37.user = auth_user_1
    django_admin_log_37.content_type = ContentType.objects.get(app_label="insurance", model="payor")
    django_admin_log_37.object_id = u'2'
    django_admin_log_37.object_repr = u'Caremark'
    django_admin_log_37.action_flag = 1
    django_admin_log_37.change_message = u''
    django_admin_log_37 = save_or_locate(django_admin_log_37)

    django_admin_log_38 = LogEntry()
    django_admin_log_38.action_time = datetime.datetime(2013, 6, 26, 3, 27, 10, tzinfo=<UTC>)
    django_admin_log_38.user = auth_user_1
    django_admin_log_38.content_type = ContentType.objects.get(app_label="insurance", model="payor")
    django_admin_log_38.object_id = u'1'
    django_admin_log_38.object_repr = u'Medco'
    django_admin_log_38.action_flag = 1
    django_admin_log_38.change_message = u''
    django_admin_log_38 = save_or_locate(django_admin_log_38)

    django_admin_log_39 = LogEntry()
    django_admin_log_39.action_time = datetime.datetime(2013, 6, 26, 3, 26, 14, tzinfo=<UTC>)
    django_admin_log_39.user = auth_user_1
    django_admin_log_39.content_type = ContentType.objects.get(app_label="drugcompanies", model="drugrep")
    django_admin_log_39.object_id = u'2'
    django_admin_log_39.object_repr = u'Mike Judge'
    django_admin_log_39.action_flag = 1
    django_admin_log_39.change_message = u''
    django_admin_log_39 = save_or_locate(django_admin_log_39)

    django_admin_log_40 = LogEntry()
    django_admin_log_40.action_time = datetime.datetime(2013, 6, 26, 3, 25, 49, tzinfo=<UTC>)
    django_admin_log_40.user = auth_user_1
    django_admin_log_40.content_type = ContentType.objects.get(app_label="drugcompanies", model="drugrep")
    django_admin_log_40.object_id = u'1'
    django_admin_log_40.object_repr = u'Lindsay Klein'
    django_admin_log_40.action_flag = 1
    django_admin_log_40.change_message = u''
    django_admin_log_40 = save_or_locate(django_admin_log_40)

    django_admin_log_41 = LogEntry()
    django_admin_log_41.action_time = datetime.datetime(2013, 6, 26, 3, 25, 21, tzinfo=<UTC>)
    django_admin_log_41.user = auth_user_1
    django_admin_log_41.content_type = ContentType.objects.get(app_label="drugcompanies", model="drugndc")
    django_admin_log_41.object_id = u'7'
    django_admin_log_41.object_repr = u'Amrix'
    django_admin_log_41.action_flag = 1
    django_admin_log_41.change_message = u''
    django_admin_log_41 = save_or_locate(django_admin_log_41)

    django_admin_log_42 = LogEntry()
    django_admin_log_42.action_time = datetime.datetime(2013, 6, 26, 3, 24, 18, tzinfo=<UTC>)
    django_admin_log_42.user = auth_user_1
    django_admin_log_42.content_type = ContentType.objects.get(app_label="drugcompanies", model="drugndc")
    django_admin_log_42.object_id = u'4'
    django_admin_log_42.object_repr = u'Fentora'
    django_admin_log_42.action_flag = 1
    django_admin_log_42.change_message = u''
    django_admin_log_42 = save_or_locate(django_admin_log_42)

    django_admin_log_43 = LogEntry()
    django_admin_log_43.action_time = datetime.datetime(2013, 6, 26, 3, 23, 22, tzinfo=<UTC>)
    django_admin_log_43.user = auth_user_1
    django_admin_log_43.content_type = ContentType.objects.get(app_label="drugcompanies", model="drugndc")
    django_admin_log_43.object_id = u'1'
    django_admin_log_43.object_repr = u'Fentora'
    django_admin_log_43.action_flag = 1
    django_admin_log_43.change_message = u''
    django_admin_log_43 = save_or_locate(django_admin_log_43)

    django_admin_log_44 = LogEntry()
    django_admin_log_44.action_time = datetime.datetime(2013, 6, 23, 5, 7, 11, tzinfo=<UTC>)
    django_admin_log_44.user = auth_user_6
    django_admin_log_44.content_type = ContentType.objects.get(app_label="appointments", model="appointment")
    django_admin_log_44.object_id = u'4'
    django_admin_log_44.object_repr = u'Fake Practice '
    django_admin_log_44.action_flag = 1
    django_admin_log_44.change_message = u''
    django_admin_log_44 = save_or_locate(django_admin_log_44)

    django_admin_log_45 = LogEntry()
    django_admin_log_45.action_time = datetime.datetime(2013, 6, 23, 5, 6, 36, tzinfo=<UTC>)
    django_admin_log_45.user = auth_user_1
    django_admin_log_45.content_type = ContentType.objects.get(app_label="appointments", model="appointment")
    django_admin_log_45.object_id = u'3'
    django_admin_log_45.object_repr = u"Craig's Practice "
    django_admin_log_45.action_flag = 1
    django_admin_log_45.change_message = u''
    django_admin_log_45 = save_or_locate(django_admin_log_45)

    django_admin_log_46 = LogEntry()
    django_admin_log_46.action_time = datetime.datetime(2013, 6, 23, 4, 49, 37, tzinfo=<UTC>)
    django_admin_log_46.user = auth_user_1
    django_admin_log_46.content_type = ContentType.objects.get(app_label="appointments", model="appointment")
    django_admin_log_46.object_id = u'2'
    django_admin_log_46.object_repr = u'Fake Practice '
    django_admin_log_46.action_flag = 2
    django_admin_log_46.change_message = u'Changed is_complete.'
    django_admin_log_46 = save_or_locate(django_admin_log_46)

    django_admin_log_47 = LogEntry()
    django_admin_log_47.action_time = datetime.datetime(2013, 6, 23, 4, 48, 33, tzinfo=<UTC>)
    django_admin_log_47.user = auth_user_1
    django_admin_log_47.content_type = ContentType.objects.get(app_label="appointments", model="appointment")
    django_admin_log_47.object_id = u'2'
    django_admin_log_47.object_repr = u'Fake Practice '
    django_admin_log_47.action_flag = 1
    django_admin_log_47.change_message = u''
    django_admin_log_47 = save_or_locate(django_admin_log_47)

    django_admin_log_48 = LogEntry()
    django_admin_log_48.action_time = datetime.datetime(2013, 6, 23, 4, 47, 38, tzinfo=<UTC>)
    django_admin_log_48.user = auth_user_6
    django_admin_log_48.content_type = ContentType.objects.get(app_label="appointments", model="appointment")
    django_admin_log_48.object_id = u'1'
    django_admin_log_48.object_repr = u'Another Practice go to there'
    django_admin_log_48.action_flag = 1
    django_admin_log_48.change_message = u''
    django_admin_log_48 = save_or_locate(django_admin_log_48)

    django_admin_log_49 = LogEntry()
    django_admin_log_49.action_time = datetime.datetime(2013, 6, 19, 18, 20, 32, tzinfo=<UTC>)
    django_admin_log_49.user = auth_user_1
    django_admin_log_49.content_type = ContentType.objects.get(app_label="tasks", model="task")
    django_admin_log_49.object_id = u'1'
    django_admin_log_49.object_repr = u'Fake Task'
    django_admin_log_49.action_flag = 3
    django_admin_log_49.change_message = u''
    django_admin_log_49 = save_or_locate(django_admin_log_49)

    django_admin_log_50 = LogEntry()
    django_admin_log_50.action_time = datetime.datetime(2013, 6, 19, 18, 9, 9, tzinfo=<UTC>)
    django_admin_log_50.user = auth_user_1
    django_admin_log_50.content_type = ContentType.objects.get(app_label="tasks", model="task")
    django_admin_log_50.object_id = u'1'
    django_admin_log_50.object_repr = u'Fake Task'
    django_admin_log_50.action_flag = 1
    django_admin_log_50.change_message = u''
    django_admin_log_50 = save_or_locate(django_admin_log_50)

    django_admin_log_51 = LogEntry()
    django_admin_log_51.action_time = datetime.datetime(2013, 6, 18, 18, 32, 15, tzinfo=<UTC>)
    django_admin_log_51.user = auth_user_1
    django_admin_log_51.content_type = ContentType.objects.get(app_label="practices", model="practice")
    django_admin_log_51.object_id = u'4'
    django_admin_log_51.object_repr = u"Craig's Practice"
    django_admin_log_51.action_flag = 1
    django_admin_log_51.change_message = u''
    django_admin_log_51 = save_or_locate(django_admin_log_51)

    django_admin_log_52 = LogEntry()
    django_admin_log_52.action_time = datetime.datetime(2013, 6, 14, 18, 49, 24, tzinfo=<UTC>)
    django_admin_log_52.user = auth_user_4
    django_admin_log_52.content_type = ContentType.objects.get(app_label="drugcompanies", model="manager")
    django_admin_log_52.object_id = u'1'
    django_admin_log_52.object_repr = u'John Harold'
    django_admin_log_52.action_flag = 1
    django_admin_log_52.change_message = u''
    django_admin_log_52 = save_or_locate(django_admin_log_52)

    django_admin_log_53 = LogEntry()
    django_admin_log_53.action_time = datetime.datetime(2013, 6, 14, 18, 47, 17, tzinfo=<UTC>)
    django_admin_log_53.user = auth_user_4
    django_admin_log_53.content_type = ContentType.objects.get(app_label="drugcompanies", model="division")
    django_admin_log_53.object_id = u'2'
    django_admin_log_53.object_repr = u'Teva Pain'
    django_admin_log_53.action_flag = 1
    django_admin_log_53.change_message = u''
    django_admin_log_53 = save_or_locate(django_admin_log_53)

    django_admin_log_54 = LogEntry()
    django_admin_log_54.action_time = datetime.datetime(2013, 6, 14, 18, 46, 23, tzinfo=<UTC>)
    django_admin_log_54.user = auth_user_4
    django_admin_log_54.content_type = ContentType.objects.get(app_label="drugcompanies", model="drug")
    django_admin_log_54.object_id = u'2'
    django_admin_log_54.object_repr = u'Amrix'
    django_admin_log_54.action_flag = 1
    django_admin_log_54.change_message = u''
    django_admin_log_54 = save_or_locate(django_admin_log_54)

    django_admin_log_55 = LogEntry()
    django_admin_log_55.action_time = datetime.datetime(2013, 6, 14, 18, 46, 12, tzinfo=<UTC>)
    django_admin_log_55.user = auth_user_4
    django_admin_log_55.content_type = ContentType.objects.get(app_label="drugcompanies", model="drug")
    django_admin_log_55.object_id = u'1'
    django_admin_log_55.object_repr = u'Fentora'
    django_admin_log_55.action_flag = 1
    django_admin_log_55.change_message = u''
    django_admin_log_55 = save_or_locate(django_admin_log_55)

    django_admin_log_56 = LogEntry()
    django_admin_log_56.action_time = datetime.datetime(2013, 6, 14, 18, 41, 59, tzinfo=<UTC>)
    django_admin_log_56.user = auth_user_4
    django_admin_log_56.content_type = ContentType.objects.get(app_label="drugcompanies", model="drugcompany")
    django_admin_log_56.object_id = u'1'
    django_admin_log_56.object_repr = u'Teva'
    django_admin_log_56.action_flag = 1
    django_admin_log_56.change_message = u''
    django_admin_log_56 = save_or_locate(django_admin_log_56)

    django_admin_log_57 = LogEntry()
    django_admin_log_57.action_time = datetime.datetime(2013, 6, 14, 13, 45, 10, tzinfo=<UTC>)
    django_admin_log_57.user = auth_user_1
    django_admin_log_57.content_type = ContentType.objects.get(app_label="regions", model="subregion")
    django_admin_log_57.object_id = u'11'
    django_admin_log_57.object_repr = u'Suffolk County'
    django_admin_log_57.action_flag = 1
    django_admin_log_57.change_message = u''
    django_admin_log_57 = save_or_locate(django_admin_log_57)

    django_admin_log_58 = LogEntry()
    django_admin_log_58.action_time = datetime.datetime(2013, 6, 14, 13, 44, 42, tzinfo=<UTC>)
    django_admin_log_58.user = auth_user_1
    django_admin_log_58.content_type = ContentType.objects.get(app_label="regions", model="subregion")
    django_admin_log_58.object_id = u'10'
    django_admin_log_58.object_repr = u'Nassau County'
    django_admin_log_58.action_flag = 1
    django_admin_log_58.change_message = u''
    django_admin_log_58 = save_or_locate(django_admin_log_58)

    django_admin_log_59 = LogEntry()
    django_admin_log_59.action_time = datetime.datetime(2013, 6, 14, 13, 44, 35, tzinfo=<UTC>)
    django_admin_log_59.user = auth_user_1
    django_admin_log_59.content_type = ContentType.objects.get(app_label="regions", model="subregion")
    django_admin_log_59.object_id = u'9'
    django_admin_log_59.object_repr = u'Buffalo'
    django_admin_log_59.action_flag = 1
    django_admin_log_59.change_message = u''
    django_admin_log_59 = save_or_locate(django_admin_log_59)

    django_admin_log_60 = LogEntry()
    django_admin_log_60.action_time = datetime.datetime(2013, 6, 14, 13, 44, 28, tzinfo=<UTC>)
    django_admin_log_60.user = auth_user_1
    django_admin_log_60.content_type = ContentType.objects.get(app_label="regions", model="subregion")
    django_admin_log_60.object_id = u'8'
    django_admin_log_60.object_repr = u'Syracuse'
    django_admin_log_60.action_flag = 1
    django_admin_log_60.change_message = u''
    django_admin_log_60 = save_or_locate(django_admin_log_60)

    django_admin_log_61 = LogEntry()
    django_admin_log_61.action_time = datetime.datetime(2013, 6, 14, 13, 43, 49, tzinfo=<UTC>)
    django_admin_log_61.user = auth_user_1
    django_admin_log_61.content_type = ContentType.objects.get(app_label="regions", model="subregion")
    django_admin_log_61.object_id = u'7'
    django_admin_log_61.object_repr = u'Upper West Side'
    django_admin_log_61.action_flag = 1
    django_admin_log_61.change_message = u''
    django_admin_log_61 = save_or_locate(django_admin_log_61)

    django_admin_log_62 = LogEntry()
    django_admin_log_62.action_time = datetime.datetime(2013, 6, 14, 13, 43, 37, tzinfo=<UTC>)
    django_admin_log_62.user = auth_user_1
    django_admin_log_62.content_type = ContentType.objects.get(app_label="regions", model="subregion")
    django_admin_log_62.object_id = u'6'
    django_admin_log_62.object_repr = u'Lower West Side'
    django_admin_log_62.action_flag = 1
    django_admin_log_62.change_message = u''
    django_admin_log_62 = save_or_locate(django_admin_log_62)

    django_admin_log_63 = LogEntry()
    django_admin_log_63.action_time = datetime.datetime(2013, 6, 14, 13, 43, 27, tzinfo=<UTC>)
    django_admin_log_63.user = auth_user_1
    django_admin_log_63.content_type = ContentType.objects.get(app_label="regions", model="subregion")
    django_admin_log_63.object_id = u'5'
    django_admin_log_63.object_repr = u'Midtown'
    django_admin_log_63.action_flag = 1
    django_admin_log_63.change_message = u''
    django_admin_log_63 = save_or_locate(django_admin_log_63)

    django_admin_log_64 = LogEntry()
    django_admin_log_64.action_time = datetime.datetime(2013, 6, 14, 13, 43, 20, tzinfo=<UTC>)
    django_admin_log_64.user = auth_user_1
    django_admin_log_64.content_type = ContentType.objects.get(app_label="regions", model="subregion")
    django_admin_log_64.object_id = u'4'
    django_admin_log_64.object_repr = u'Lower East Side'
    django_admin_log_64.action_flag = 1
    django_admin_log_64.change_message = u''
    django_admin_log_64 = save_or_locate(django_admin_log_64)

    django_admin_log_65 = LogEntry()
    django_admin_log_65.action_time = datetime.datetime(2013, 6, 14, 13, 43, 6, tzinfo=<UTC>)
    django_admin_log_65.user = auth_user_1
    django_admin_log_65.content_type = ContentType.objects.get(app_label="regions", model="subregion")
    django_admin_log_65.object_id = u'3'
    django_admin_log_65.object_repr = u'Upper East Side'
    django_admin_log_65.action_flag = 1
    django_admin_log_65.change_message = u''
    django_admin_log_65 = save_or_locate(django_admin_log_65)

    django_admin_log_66 = LogEntry()
    django_admin_log_66.action_time = datetime.datetime(2013, 6, 14, 13, 42, 34, tzinfo=<UTC>)
    django_admin_log_66.user = auth_user_1
    django_admin_log_66.content_type = ContentType.objects.get(app_label="regions", model="subregion")
    django_admin_log_66.object_id = u'2'
    django_admin_log_66.object_repr = u'North Jersey'
    django_admin_log_66.action_flag = 1
    django_admin_log_66.change_message = u''
    django_admin_log_66 = save_or_locate(django_admin_log_66)

    django_admin_log_67 = LogEntry()
    django_admin_log_67.action_time = datetime.datetime(2013, 6, 14, 13, 42, 24, tzinfo=<UTC>)
    django_admin_log_67.user = auth_user_1
    django_admin_log_67.content_type = ContentType.objects.get(app_label="regions", model="subregion")
    django_admin_log_67.object_id = u'1'
    django_admin_log_67.object_repr = u'South Jersey'
    django_admin_log_67.action_flag = 1
    django_admin_log_67.change_message = u''
    django_admin_log_67 = save_or_locate(django_admin_log_67)

    django_admin_log_68 = LogEntry()
    django_admin_log_68.action_time = datetime.datetime(2013, 6, 14, 13, 41, 52, tzinfo=<UTC>)
    django_admin_log_68.user = auth_user_1
    django_admin_log_68.content_type = ContentType.objects.get(app_label="regions", model="region")
    django_admin_log_68.object_id = u'24'
    django_admin_log_68.object_repr = u'Ohio'
    django_admin_log_68.action_flag = 1
    django_admin_log_68.change_message = u''
    django_admin_log_68 = save_or_locate(django_admin_log_68)

    django_admin_log_69 = LogEntry()
    django_admin_log_69.action_time = datetime.datetime(2013, 6, 14, 13, 41, 50, tzinfo=<UTC>)
    django_admin_log_69.user = auth_user_1
    django_admin_log_69.content_type = ContentType.objects.get(app_label="regions", model="region")
    django_admin_log_69.object_id = u'23'
    django_admin_log_69.object_repr = u'Louisiana'
    django_admin_log_69.action_flag = 1
    django_admin_log_69.change_message = u''
    django_admin_log_69 = save_or_locate(django_admin_log_69)

    django_admin_log_70 = LogEntry()
    django_admin_log_70.action_time = datetime.datetime(2013, 6, 14, 13, 41, 45, tzinfo=<UTC>)
    django_admin_log_70.user = auth_user_1
    django_admin_log_70.content_type = ContentType.objects.get(app_label="regions", model="region")
    django_admin_log_70.object_id = u'22'
    django_admin_log_70.object_repr = u'Wisconsin'
    django_admin_log_70.action_flag = 1
    django_admin_log_70.change_message = u''
    django_admin_log_70 = save_or_locate(django_admin_log_70)

    django_admin_log_71 = LogEntry()
    django_admin_log_71.action_time = datetime.datetime(2013, 6, 14, 13, 41, 40, tzinfo=<UTC>)
    django_admin_log_71.user = auth_user_1
    django_admin_log_71.content_type = ContentType.objects.get(app_label="regions", model="region")
    django_admin_log_71.object_id = u'21'
    django_admin_log_71.object_repr = u'Kentucky'
    django_admin_log_71.action_flag = 1
    django_admin_log_71.change_message = u''
    django_admin_log_71 = save_or_locate(django_admin_log_71)

    django_admin_log_72 = LogEntry()
    django_admin_log_72.action_time = datetime.datetime(2013, 6, 14, 13, 41, 34, tzinfo=<UTC>)
    django_admin_log_72.user = auth_user_1
    django_admin_log_72.content_type = ContentType.objects.get(app_label="regions", model="region")
    django_admin_log_72.object_id = u'20'
    django_admin_log_72.object_repr = u'Colorado'
    django_admin_log_72.action_flag = 1
    django_admin_log_72.change_message = u''
    django_admin_log_72 = save_or_locate(django_admin_log_72)

    django_admin_log_73 = LogEntry()
    django_admin_log_73.action_time = datetime.datetime(2013, 6, 14, 13, 41, 30, tzinfo=<UTC>)
    django_admin_log_73.user = auth_user_1
    django_admin_log_73.content_type = ContentType.objects.get(app_label="regions", model="region")
    django_admin_log_73.object_id = u'19'
    django_admin_log_73.object_repr = u'Maryland'
    django_admin_log_73.action_flag = 1
    django_admin_log_73.change_message = u''
    django_admin_log_73 = save_or_locate(django_admin_log_73)

    django_admin_log_74 = LogEntry()
    django_admin_log_74.action_time = datetime.datetime(2013, 6, 14, 13, 41, 22, tzinfo=<UTC>)
    django_admin_log_74.user = auth_user_1
    django_admin_log_74.content_type = ContentType.objects.get(app_label="regions", model="region")
    django_admin_log_74.object_id = u'18'
    django_admin_log_74.object_repr = u'Illinois'
    django_admin_log_74.action_flag = 1
    django_admin_log_74.change_message = u''
    django_admin_log_74 = save_or_locate(django_admin_log_74)

    django_admin_log_75 = LogEntry()
    django_admin_log_75.action_time = datetime.datetime(2013, 6, 14, 13, 41, 16, tzinfo=<UTC>)
    django_admin_log_75.user = auth_user_1
    django_admin_log_75.content_type = ContentType.objects.get(app_label="regions", model="region")
    django_admin_log_75.object_id = u'17'
    django_admin_log_75.object_repr = u'Indiana'
    django_admin_log_75.action_flag = 1
    django_admin_log_75.change_message = u''
    django_admin_log_75 = save_or_locate(django_admin_log_75)

    django_admin_log_76 = LogEntry()
    django_admin_log_76.action_time = datetime.datetime(2013, 6, 14, 13, 41, 8, tzinfo=<UTC>)
    django_admin_log_76.user = auth_user_1
    django_admin_log_76.content_type = ContentType.objects.get(app_label="regions", model="region")
    django_admin_log_76.object_id = u'16'
    django_admin_log_76.object_repr = u'Michigan'
    django_admin_log_76.action_flag = 1
    django_admin_log_76.change_message = u''
    django_admin_log_76 = save_or_locate(django_admin_log_76)

    django_admin_log_77 = LogEntry()
    django_admin_log_77.action_time = datetime.datetime(2013, 6, 14, 13, 41, 4, tzinfo=<UTC>)
    django_admin_log_77.user = auth_user_1
    django_admin_log_77.content_type = ContentType.objects.get(app_label="regions", model="region")
    django_admin_log_77.object_id = u'15'
    django_admin_log_77.object_repr = u'Alabama'
    django_admin_log_77.action_flag = 1
    django_admin_log_77.change_message = u''
    django_admin_log_77 = save_or_locate(django_admin_log_77)

    django_admin_log_78 = LogEntry()
    django_admin_log_78.action_time = datetime.datetime(2013, 6, 14, 13, 40, 58, tzinfo=<UTC>)
    django_admin_log_78.user = auth_user_1
    django_admin_log_78.content_type = ContentType.objects.get(app_label="regions", model="region")
    django_admin_log_78.object_id = u'14'
    django_admin_log_78.object_repr = u'Deleware'
    django_admin_log_78.action_flag = 1
    django_admin_log_78.change_message = u''
    django_admin_log_78 = save_or_locate(django_admin_log_78)

    django_admin_log_79 = LogEntry()
    django_admin_log_79.action_time = datetime.datetime(2013, 6, 14, 13, 40, 52, tzinfo=<UTC>)
    django_admin_log_79.user = auth_user_1
    django_admin_log_79.content_type = ContentType.objects.get(app_label="regions", model="region")
    django_admin_log_79.object_id = u'13'
    django_admin_log_79.object_repr = u'North Carolina'
    django_admin_log_79.action_flag = 1
    django_admin_log_79.change_message = u''
    django_admin_log_79 = save_or_locate(django_admin_log_79)

    django_admin_log_80 = LogEntry()
    django_admin_log_80.action_time = datetime.datetime(2013, 6, 14, 13, 40, 46, tzinfo=<UTC>)
    django_admin_log_80.user = auth_user_1
    django_admin_log_80.content_type = ContentType.objects.get(app_label="regions", model="region")
    django_admin_log_80.object_id = u'12'
    django_admin_log_80.object_repr = u'Arkansas'
    django_admin_log_80.action_flag = 1
    django_admin_log_80.change_message = u''
    django_admin_log_80 = save_or_locate(django_admin_log_80)

    django_admin_log_81 = LogEntry()
    django_admin_log_81.action_time = datetime.datetime(2013, 6, 14, 13, 40, 40, tzinfo=<UTC>)
    django_admin_log_81.user = auth_user_1
    django_admin_log_81.content_type = ContentType.objects.get(app_label="regions", model="region")
    django_admin_log_81.object_id = u'11'
    django_admin_log_81.object_repr = u'Georgia'
    django_admin_log_81.action_flag = 1
    django_admin_log_81.change_message = u''
    django_admin_log_81 = save_or_locate(django_admin_log_81)

    django_admin_log_82 = LogEntry()
    django_admin_log_82.action_time = datetime.datetime(2013, 6, 14, 13, 40, 35, tzinfo=<UTC>)
    django_admin_log_82.user = auth_user_1
    django_admin_log_82.content_type = ContentType.objects.get(app_label="regions", model="region")
    django_admin_log_82.object_id = u'10'
    django_admin_log_82.object_repr = u'Connecticut'
    django_admin_log_82.action_flag = 1
    django_admin_log_82.change_message = u''
    django_admin_log_82 = save_or_locate(django_admin_log_82)

    django_admin_log_83 = LogEntry()
    django_admin_log_83.action_time = datetime.datetime(2013, 6, 14, 13, 37, 32, tzinfo=<UTC>)
    django_admin_log_83.user = auth_user_1
    django_admin_log_83.content_type = ContentType.objects.get(app_label="regions", model="region")
    django_admin_log_83.object_id = u'9'
    django_admin_log_83.object_repr = u'Florida'
    django_admin_log_83.action_flag = 1
    django_admin_log_83.change_message = u''
    django_admin_log_83 = save_or_locate(django_admin_log_83)

    django_admin_log_84 = LogEntry()
    django_admin_log_84.action_time = datetime.datetime(2013, 6, 14, 13, 37, 26, tzinfo=<UTC>)
    django_admin_log_84.user = auth_user_1
    django_admin_log_84.content_type = ContentType.objects.get(app_label="regions", model="region")
    django_admin_log_84.object_id = u'8'
    django_admin_log_84.object_repr = u'Massachusetts'
    django_admin_log_84.action_flag = 1
    django_admin_log_84.change_message = u''
    django_admin_log_84 = save_or_locate(django_admin_log_84)

    django_admin_log_85 = LogEntry()
    django_admin_log_85.action_time = datetime.datetime(2013, 6, 14, 13, 36, 54, tzinfo=<UTC>)
    django_admin_log_85.user = auth_user_1
    django_admin_log_85.content_type = ContentType.objects.get(app_label="regions", model="region")
    django_admin_log_85.object_id = u'7'
    django_admin_log_85.object_repr = u'New Jersey'
    django_admin_log_85.action_flag = 1
    django_admin_log_85.change_message = u''
    django_admin_log_85 = save_or_locate(django_admin_log_85)

    django_admin_log_86 = LogEntry()
    django_admin_log_86.action_time = datetime.datetime(2013, 6, 14, 13, 36, 39, tzinfo=<UTC>)
    django_admin_log_86.user = auth_user_1
    django_admin_log_86.content_type = ContentType.objects.get(app_label="regions", model="region")
    django_admin_log_86.object_id = u'6'
    django_admin_log_86.object_repr = u'Upstate New York'
    django_admin_log_86.action_flag = 1
    django_admin_log_86.change_message = u''
    django_admin_log_86 = save_or_locate(django_admin_log_86)

    django_admin_log_87 = LogEntry()
    django_admin_log_87.action_time = datetime.datetime(2013, 6, 14, 13, 36, 26, tzinfo=<UTC>)
    django_admin_log_87.user = auth_user_1
    django_admin_log_87.content_type = ContentType.objects.get(app_label="regions", model="region")
    django_admin_log_87.object_id = u'5'
    django_admin_log_87.object_repr = u'Long Island'
    django_admin_log_87.action_flag = 2
    django_admin_log_87.change_message = u'Changed name.'
    django_admin_log_87 = save_or_locate(django_admin_log_87)

    django_admin_log_88 = LogEntry()
    django_admin_log_88.action_time = datetime.datetime(2013, 6, 14, 13, 36, 11, tzinfo=<UTC>)
    django_admin_log_88.user = auth_user_1
    django_admin_log_88.content_type = ContentType.objects.get(app_label="regions", model="region")
    django_admin_log_88.object_id = u'5'
    django_admin_log_88.object_repr = u'Nassau County'
    django_admin_log_88.action_flag = 1
    django_admin_log_88.change_message = u''
    django_admin_log_88 = save_or_locate(django_admin_log_88)

    django_admin_log_89 = LogEntry()
    django_admin_log_89.action_time = datetime.datetime(2013, 6, 14, 13, 35, 33, tzinfo=<UTC>)
    django_admin_log_89.user = auth_user_1
    django_admin_log_89.content_type = ContentType.objects.get(app_label="regions", model="region")
    django_admin_log_89.object_id = u'4'
    django_admin_log_89.object_repr = u'Bronx'
    django_admin_log_89.action_flag = 1
    django_admin_log_89.change_message = u''
    django_admin_log_89 = save_or_locate(django_admin_log_89)

    django_admin_log_90 = LogEntry()
    django_admin_log_90.action_time = datetime.datetime(2013, 6, 14, 13, 35, 27, tzinfo=<UTC>)
    django_admin_log_90.user = auth_user_1
    django_admin_log_90.content_type = ContentType.objects.get(app_label="regions", model="region")
    django_admin_log_90.object_id = u'3'
    django_admin_log_90.object_repr = u'Queens'
    django_admin_log_90.action_flag = 1
    django_admin_log_90.change_message = u''
    django_admin_log_90 = save_or_locate(django_admin_log_90)

    django_admin_log_91 = LogEntry()
    django_admin_log_91.action_time = datetime.datetime(2013, 6, 14, 13, 35, 22, tzinfo=<UTC>)
    django_admin_log_91.user = auth_user_1
    django_admin_log_91.content_type = ContentType.objects.get(app_label="regions", model="region")
    django_admin_log_91.object_id = u'2'
    django_admin_log_91.object_repr = u'Brooklyn'
    django_admin_log_91.action_flag = 1
    django_admin_log_91.change_message = u''
    django_admin_log_91 = save_or_locate(django_admin_log_91)

    django_admin_log_92 = LogEntry()
    django_admin_log_92.action_time = datetime.datetime(2013, 6, 14, 13, 35, 3, tzinfo=<UTC>)
    django_admin_log_92.user = auth_user_1
    django_admin_log_92.content_type = ContentType.objects.get(app_label="regions", model="region")
    django_admin_log_92.object_id = u'1'
    django_admin_log_92.object_repr = u'Manhattan'
    django_admin_log_92.action_flag = 1
    django_admin_log_92.change_message = u''
    django_admin_log_92 = save_or_locate(django_admin_log_92)

    django_admin_log_93 = LogEntry()
    django_admin_log_93.action_time = datetime.datetime(2013, 6, 14, 4, 35, 10, tzinfo=<UTC>)
    django_admin_log_93.user = auth_user_1
    django_admin_log_93.content_type = ContentType.objects.get(app_label="salesreps", model="commissiontagsplit")
    django_admin_log_93.object_id = u'6'
    django_admin_log_93.object_repr = u'BP 0.0075'
    django_admin_log_93.action_flag = 1
    django_admin_log_93.change_message = u''
    django_admin_log_93 = save_or_locate(django_admin_log_93)

    django_admin_log_94 = LogEntry()
    django_admin_log_94.action_time = datetime.datetime(2013, 6, 14, 4, 34, 45, tzinfo=<UTC>)
    django_admin_log_94.user = auth_user_1
    django_admin_log_94.content_type = ContentType.objects.get(app_label="salesreps", model="commissiontagsplit")
    django_admin_log_94.object_id = u'5'
    django_admin_log_94.object_repr = u'BP 0.0075'
    django_admin_log_94.action_flag = 1
    django_admin_log_94.change_message = u''
    django_admin_log_94 = save_or_locate(django_admin_log_94)

    django_admin_log_95 = LogEntry()
    django_admin_log_95.action_time = datetime.datetime(2013, 6, 14, 4, 34, 4, tzinfo=<UTC>)
    django_admin_log_95.user = auth_user_1
    django_admin_log_95.content_type = ContentType.objects.get(app_label="auth", model="user")
    django_admin_log_95.object_id = u'6'
    django_admin_log_95.object_repr = u'pblock'
    django_admin_log_95.action_flag = 2
    django_admin_log_95.change_message = u'Changed password, first_name, last_name, is_staff and groups.'
    django_admin_log_95 = save_or_locate(django_admin_log_95)

    django_admin_log_96 = LogEntry()
    django_admin_log_96.action_time = datetime.datetime(2013, 6, 14, 4, 33, 38, tzinfo=<UTC>)
    django_admin_log_96.user = auth_user_1
    django_admin_log_96.content_type = ContentType.objects.get(app_label="auth", model="user")
    django_admin_log_96.object_id = u'6'
    django_admin_log_96.object_repr = u'pblock'
    django_admin_log_96.action_flag = 1
    django_admin_log_96.change_message = u''
    django_admin_log_96 = save_or_locate(django_admin_log_96)

    django_admin_log_97 = LogEntry()
    django_admin_log_97.action_time = datetime.datetime(2013, 6, 14, 4, 32, 59, tzinfo=<UTC>)
    django_admin_log_97.user = auth_user_1
    django_admin_log_97.content_type = ContentType.objects.get(app_label="salesreps", model="commissiontagsplit")
    django_admin_log_97.object_id = u'4'
    django_admin_log_97.object_repr = u'BP 0.0075'
    django_admin_log_97.action_flag = 1
    django_admin_log_97.change_message = u''
    django_admin_log_97 = save_or_locate(django_admin_log_97)

    django_admin_log_98 = LogEntry()
    django_admin_log_98.action_time = datetime.datetime(2013, 6, 14, 4, 32, 35, tzinfo=<UTC>)
    django_admin_log_98.user = auth_user_1
    django_admin_log_98.content_type = ContentType.objects.get(app_label="salesreps", model="commissiontagsplit")
    django_admin_log_98.object_id = u'3'
    django_admin_log_98.object_repr = u'FB 0.0075'
    django_admin_log_98.action_flag = 1
    django_admin_log_98.change_message = u''
    django_admin_log_98 = save_or_locate(django_admin_log_98)

    django_admin_log_99 = LogEntry()
    django_admin_log_99.action_time = datetime.datetime(2013, 6, 14, 4, 30, 47, tzinfo=<UTC>)
    django_admin_log_99.user = auth_user_1
    django_admin_log_99.content_type = ContentType.objects.get(app_label="salesreps", model="commissiontagsplit")
    django_admin_log_99.object_id = u'2'
    django_admin_log_99.object_repr = u'0.015 0.015'
    django_admin_log_99.action_flag = 1
    django_admin_log_99.change_message = u''
    django_admin_log_99 = save_or_locate(django_admin_log_99)

    django_admin_log_100 = LogEntry()
    django_admin_log_100.action_time = datetime.datetime(2013, 6, 14, 4, 28, 53, tzinfo=<UTC>)
    django_admin_log_100.user = auth_user_1
    django_admin_log_100.content_type = ContentType.objects.get(app_label="salesreps", model="commissiontag")
    django_admin_log_100.object_id = u'4'
    django_admin_log_100.object_repr = u'FB'
    django_admin_log_100.action_flag = 1
    django_admin_log_100.change_message = u''
    django_admin_log_100 = save_or_locate(django_admin_log_100)

    django_admin_log_101 = LogEntry()
    django_admin_log_101.action_time = datetime.datetime(2013, 6, 14, 4, 28, 44, tzinfo=<UTC>)
    django_admin_log_101.user = auth_user_1
    django_admin_log_101.content_type = ContentType.objects.get(app_label="salesreps", model="commissiontag")
    django_admin_log_101.object_id = u'3'
    django_admin_log_101.object_repr = u'BP'
    django_admin_log_101.action_flag = 1
    django_admin_log_101.change_message = u''
    django_admin_log_101 = save_or_locate(django_admin_log_101)

    django_admin_log_102 = LogEntry()
    django_admin_log_102.action_time = datetime.datetime(2013, 6, 14, 4, 28, 35, tzinfo=<UTC>)
    django_admin_log_102.user = auth_user_1
    django_admin_log_102.content_type = ContentType.objects.get(app_label="salesreps", model="commissiontag")
    django_admin_log_102.object_id = u'2'
    django_admin_log_102.object_repr = u'PB'
    django_admin_log_102.action_flag = 1
    django_admin_log_102.change_message = u''
    django_admin_log_102 = save_or_locate(django_admin_log_102)

    django_admin_log_103 = LogEntry()
    django_admin_log_103.action_time = datetime.datetime(2013, 6, 14, 4, 28, 29, tzinfo=<UTC>)
    django_admin_log_103.user = auth_user_1
    django_admin_log_103.content_type = ContentType.objects.get(app_label="salesreps", model="commissiontag")
    django_admin_log_103.object_id = u'1'
    django_admin_log_103.object_repr = u'BB'
    django_admin_log_103.action_flag = 1
    django_admin_log_103.change_message = u''
    django_admin_log_103 = save_or_locate(django_admin_log_103)

    django_admin_log_104 = LogEntry()
    django_admin_log_104.action_time = datetime.datetime(2013, 6, 14, 4, 28, 6, tzinfo=<UTC>)
    django_admin_log_104.user = auth_user_1
    django_admin_log_104.content_type = ContentType.objects.get(app_label="practices", model="category")
    django_admin_log_104.object_id = u'3'
    django_admin_log_104.object_repr = u'Rheumatology'
    django_admin_log_104.action_flag = 1
    django_admin_log_104.change_message = u''
    django_admin_log_104 = save_or_locate(django_admin_log_104)

    django_admin_log_105 = LogEntry()
    django_admin_log_105.action_time = datetime.datetime(2013, 6, 14, 4, 27, 54, tzinfo=<UTC>)
    django_admin_log_105.user = auth_user_1
    django_admin_log_105.content_type = ContentType.objects.get(app_label="practices", model="category")
    django_admin_log_105.object_id = u'2'
    django_admin_log_105.object_repr = u'Oncology'
    django_admin_log_105.action_flag = 1
    django_admin_log_105.change_message = u''
    django_admin_log_105 = save_or_locate(django_admin_log_105)

    django_admin_log_106 = LogEntry()
    django_admin_log_106.action_time = datetime.datetime(2013, 6, 14, 4, 27, 45, tzinfo=<UTC>)
    django_admin_log_106.user = auth_user_1
    django_admin_log_106.content_type = ContentType.objects.get(app_label="practices", model="category")
    django_admin_log_106.object_id = u'1'
    django_admin_log_106.object_repr = u'Pain'
    django_admin_log_106.action_flag = 1
    django_admin_log_106.change_message = u''
    django_admin_log_106 = save_or_locate(django_admin_log_106)

    django_admin_log_107 = LogEntry()
    django_admin_log_107.action_time = datetime.datetime(2013, 6, 14, 4, 26, 57, tzinfo=<UTC>)
    django_admin_log_107.user = auth_user_1
    django_admin_log_107.content_type = ContentType.objects.get(app_label="payments", model="paymenttype")
    django_admin_log_107.object_id = u'5'
    django_admin_log_107.object_repr = u'E-Voucher Upload'
    django_admin_log_107.action_flag = 1
    django_admin_log_107.change_message = u''
    django_admin_log_107 = save_or_locate(django_admin_log_107)

    django_admin_log_108 = LogEntry()
    django_admin_log_108.action_time = datetime.datetime(2013, 6, 14, 4, 26, 42, tzinfo=<UTC>)
    django_admin_log_108.user = auth_user_1
    django_admin_log_108.content_type = ContentType.objects.get(app_label="payments", model="paymenttype")
    django_admin_log_108.object_id = u'4'
    django_admin_log_108.object_repr = u'Upload'
    django_admin_log_108.action_flag = 1
    django_admin_log_108.change_message = u''
    django_admin_log_108 = save_or_locate(django_admin_log_108)

    django_admin_log_109 = LogEntry()
    django_admin_log_109.action_time = datetime.datetime(2013, 6, 14, 4, 26, 36, tzinfo=<UTC>)
    django_admin_log_109.user = auth_user_1
    django_admin_log_109.content_type = ContentType.objects.get(app_label="payments", model="paymenttype")
    django_admin_log_109.object_id = u'3'
    django_admin_log_109.object_repr = u'Write Down'
    django_admin_log_109.action_flag = 1
    django_admin_log_109.change_message = u''
    django_admin_log_109 = save_or_locate(django_admin_log_109)

    django_admin_log_110 = LogEntry()
    django_admin_log_110.action_time = datetime.datetime(2013, 6, 14, 4, 26, 29, tzinfo=<UTC>)
    django_admin_log_110.user = auth_user_1
    django_admin_log_110.content_type = ContentType.objects.get(app_label="payments", model="paymenttype")
    django_admin_log_110.object_id = u'2'
    django_admin_log_110.object_repr = u'Manual'
    django_admin_log_110.action_flag = 1
    django_admin_log_110.change_message = u''
    django_admin_log_110 = save_or_locate(django_admin_log_110)

    django_admin_log_111 = LogEntry()
    django_admin_log_111.action_time = datetime.datetime(2013, 6, 14, 4, 26, 17, tzinfo=<UTC>)
    django_admin_log_111.user = auth_user_1
    django_admin_log_111.content_type = ContentType.objects.get(app_label="payments", model="paymenttype")
    django_admin_log_111.object_id = u'1'
    django_admin_log_111.object_repr = u'835'
    django_admin_log_111.action_flag = 1
    django_admin_log_111.change_message = u''
    django_admin_log_111 = save_or_locate(django_admin_log_111)

    django_admin_log_112 = LogEntry()
    django_admin_log_112.action_time = datetime.datetime(2013, 6, 14, 4, 25, 29, tzinfo=<UTC>)
    django_admin_log_112.user = auth_user_1
    django_admin_log_112.content_type = ContentType.objects.get(app_label="practices", model="contacttype")
    django_admin_log_112.object_id = u'4'
    django_admin_log_112.object_repr = u'Other'
    django_admin_log_112.action_flag = 1
    django_admin_log_112.change_message = u''
    django_admin_log_112 = save_or_locate(django_admin_log_112)

    django_admin_log_113 = LogEntry()
    django_admin_log_113.action_time = datetime.datetime(2013, 6, 14, 4, 25, 13, tzinfo=<UTC>)
    django_admin_log_113.user = auth_user_1
    django_admin_log_113.content_type = ContentType.objects.get(app_label="practices", model="contacttype")
    django_admin_log_113.object_id = u'3'
    django_admin_log_113.object_repr = u'Receptionist'
    django_admin_log_113.action_flag = 1
    django_admin_log_113.change_message = u''
    django_admin_log_113 = save_or_locate(django_admin_log_113)

    django_admin_log_114 = LogEntry()
    django_admin_log_114.action_time = datetime.datetime(2013, 6, 14, 4, 25, 4, tzinfo=<UTC>)
    django_admin_log_114.user = auth_user_1
    django_admin_log_114.content_type = ContentType.objects.get(app_label="practices", model="contacttype")
    django_admin_log_114.object_id = u'2'
    django_admin_log_114.object_repr = u'Nurse'
    django_admin_log_114.action_flag = 1
    django_admin_log_114.change_message = u''
    django_admin_log_114 = save_or_locate(django_admin_log_114)

    django_admin_log_115 = LogEntry()
    django_admin_log_115.action_time = datetime.datetime(2013, 6, 14, 4, 23, 11, tzinfo=<UTC>)
    django_admin_log_115.user = auth_user_1
    django_admin_log_115.content_type = ContentType.objects.get(app_label="interactions", model="interactiontype")
    django_admin_log_115.object_id = u'3'
    django_admin_log_115.object_repr = u'Text Message'
    django_admin_log_115.action_flag = 1
    django_admin_log_115.change_message = u''
    django_admin_log_115 = save_or_locate(django_admin_log_115)

    django_admin_log_116 = LogEntry()
    django_admin_log_116.action_time = datetime.datetime(2013, 6, 14, 4, 23, 3, tzinfo=<UTC>)
    django_admin_log_116.user = auth_user_1
    django_admin_log_116.content_type = ContentType.objects.get(app_label="interactions", model="interactiontype")
    django_admin_log_116.object_id = u'2'
    django_admin_log_116.object_repr = u'E-mail'
    django_admin_log_116.action_flag = 1
    django_admin_log_116.change_message = u''
    django_admin_log_116 = save_or_locate(django_admin_log_116)

    django_admin_log_117 = LogEntry()
    django_admin_log_117.action_time = datetime.datetime(2013, 6, 14, 4, 22, 54, tzinfo=<UTC>)
    django_admin_log_117.user = auth_user_1
    django_admin_log_117.content_type = ContentType.objects.get(app_label="interactions", model="interactiontype")
    django_admin_log_117.object_id = u'1'
    django_admin_log_117.object_repr = u'Phone Call'
    django_admin_log_117.action_flag = 1
    django_admin_log_117.change_message = u''
    django_admin_log_117 = save_or_locate(django_admin_log_117)

    django_admin_log_118 = LogEntry()
    django_admin_log_118.action_time = datetime.datetime(2013, 6, 13, 16, 48, 4, tzinfo=<UTC>)
    django_admin_log_118.user = auth_user_1
    django_admin_log_118.content_type = ContentType.objects.get(app_label="practices", model="contacttype")
    django_admin_log_118.object_id = u'1'
    django_admin_log_118.object_repr = u'Office Manager'
    django_admin_log_118.action_flag = 1
    django_admin_log_118.change_message = u''
    django_admin_log_118 = save_or_locate(django_admin_log_118)

    django_admin_log_119 = LogEntry()
    django_admin_log_119.action_time = datetime.datetime(2013, 6, 12, 23, 45, 39, tzinfo=<UTC>)
    django_admin_log_119.user = auth_user_1
    django_admin_log_119.content_type = ContentType.objects.get(app_label="practices", model="practice")
    django_admin_log_119.object_id = u'3'
    django_admin_log_119.object_repr = u'Another Practice'
    django_admin_log_119.action_flag = 2
    django_admin_log_119.change_message = u'Changed is_inactive.'
    django_admin_log_119 = save_or_locate(django_admin_log_119)

    django_admin_log_120 = LogEntry()
    django_admin_log_120.action_time = datetime.datetime(2013, 6, 12, 23, 45, 12, tzinfo=<UTC>)
    django_admin_log_120.user = auth_user_1
    django_admin_log_120.content_type = ContentType.objects.get(app_label="practices", model="practice")
    django_admin_log_120.object_id = u'3'
    django_admin_log_120.object_repr = u'Another Practice'
    django_admin_log_120.action_flag = 1
    django_admin_log_120.change_message = u''
    django_admin_log_120 = save_or_locate(django_admin_log_120)

    django_admin_log_121 = LogEntry()
    django_admin_log_121.action_time = datetime.datetime(2013, 6, 12, 23, 44, 32, tzinfo=<UTC>)
    django_admin_log_121.user = auth_user_1
    django_admin_log_121.content_type = ContentType.objects.get(app_label="auth", model="user")
    django_admin_log_121.object_id = u'1'
    django_admin_log_121.object_repr = u'ccohen'
    django_admin_log_121.action_flag = 2
    django_admin_log_121.change_message = u'Changed password and groups.'
    django_admin_log_121 = save_or_locate(django_admin_log_121)

    django_admin_log_122 = LogEntry()
    django_admin_log_122.action_time = datetime.datetime(2013, 6, 12, 23, 44, 14, tzinfo=<UTC>)
    django_admin_log_122.user = auth_user_1
    django_admin_log_122.content_type = ContentType.objects.get(app_label="auth", model="user")
    django_admin_log_122.object_id = u'1'
    django_admin_log_122.object_repr = u'ccohen'
    django_admin_log_122.action_flag = 2
    django_admin_log_122.change_message = u'Changed password, first_name and last_name.'
    django_admin_log_122 = save_or_locate(django_admin_log_122)

    django_admin_log_123 = LogEntry()
    django_admin_log_123.action_time = datetime.datetime(2013, 6, 12, 22, 39, 52, tzinfo=<UTC>)
    django_admin_log_123.user = auth_user_1
    django_admin_log_123.content_type = ContentType.objects.get(app_label="practices", model="practice")
    django_admin_log_123.object_id = u'2'
    django_admin_log_123.object_repr = u'Fake Practice'
    django_admin_log_123.action_flag = 1
    django_admin_log_123.change_message = u''
    django_admin_log_123 = save_or_locate(django_admin_log_123)

    django_admin_log_124 = LogEntry()
    django_admin_log_124.action_time = datetime.datetime(2013, 6, 11, 15, 25, 27, tzinfo=<UTC>)
    django_admin_log_124.user = auth_user_1
    django_admin_log_124.content_type = ContentType.objects.get(app_label="auth", model="user")
    django_admin_log_124.object_id = u'5'
    django_admin_log_124.object_repr = u'cleibowitz'
    django_admin_log_124.action_flag = 2
    django_admin_log_124.change_message = u'Changed password, first_name, last_name, email, is_staff and groups.'
    django_admin_log_124 = save_or_locate(django_admin_log_124)

    django_admin_log_125 = LogEntry()
    django_admin_log_125.action_time = datetime.datetime(2013, 6, 11, 15, 25, 5, tzinfo=<UTC>)
    django_admin_log_125.user = auth_user_1
    django_admin_log_125.content_type = ContentType.objects.get(app_label="auth", model="user")
    django_admin_log_125.object_id = u'5'
    django_admin_log_125.object_repr = u'cleibowitz'
    django_admin_log_125.action_flag = 1
    django_admin_log_125.change_message = u''
    django_admin_log_125 = save_or_locate(django_admin_log_125)

    django_admin_log_126 = LogEntry()
    django_admin_log_126.action_time = datetime.datetime(2013, 6, 11, 15, 24, 30, tzinfo=<UTC>)
    django_admin_log_126.user = auth_user_1
    django_admin_log_126.content_type = ContentType.objects.get(app_label="auth", model="user")
    django_admin_log_126.object_id = u'4'
    django_admin_log_126.object_repr = u'gbortnick'
    django_admin_log_126.action_flag = 2
    django_admin_log_126.change_message = u'Changed password, first_name, last_name, email, is_staff and groups.'
    django_admin_log_126 = save_or_locate(django_admin_log_126)

    django_admin_log_127 = LogEntry()
    django_admin_log_127.action_time = datetime.datetime(2013, 6, 11, 15, 24, 4, tzinfo=<UTC>)
    django_admin_log_127.user = auth_user_1
    django_admin_log_127.content_type = ContentType.objects.get(app_label="auth", model="user")
    django_admin_log_127.object_id = u'4'
    django_admin_log_127.object_repr = u'gbortnick'
    django_admin_log_127.action_flag = 1
    django_admin_log_127.change_message = u''
    django_admin_log_127 = save_or_locate(django_admin_log_127)

    django_admin_log_128 = LogEntry()
    django_admin_log_128.action_time = datetime.datetime(2013, 6, 11, 15, 23, 46, tzinfo=<UTC>)
    django_admin_log_128.user = auth_user_1
    django_admin_log_128.content_type = ContentType.objects.get(app_label="auth", model="user")
    django_admin_log_128.object_id = u'3'
    django_admin_log_128.object_repr = u'bbloom'
    django_admin_log_128.action_flag = 2
    django_admin_log_128.change_message = u'Changed password, first_name, last_name, email and is_staff.'
    django_admin_log_128 = save_or_locate(django_admin_log_128)

    django_admin_log_129 = LogEntry()
    django_admin_log_129.action_time = datetime.datetime(2013, 6, 11, 15, 23, 27, tzinfo=<UTC>)
    django_admin_log_129.user = auth_user_1
    django_admin_log_129.content_type = ContentType.objects.get(app_label="auth", model="user")
    django_admin_log_129.object_id = u'3'
    django_admin_log_129.object_repr = u'bbloom'
    django_admin_log_129.action_flag = 2
    django_admin_log_129.change_message = u'Changed password and groups.'
    django_admin_log_129 = save_or_locate(django_admin_log_129)

    django_admin_log_130 = LogEntry()
    django_admin_log_130.action_time = datetime.datetime(2013, 6, 11, 15, 23, 14, tzinfo=<UTC>)
    django_admin_log_130.user = auth_user_1
    django_admin_log_130.content_type = ContentType.objects.get(app_label="auth", model="user")
    django_admin_log_130.object_id = u'3'
    django_admin_log_130.object_repr = u'bbloom'
    django_admin_log_130.action_flag = 1
    django_admin_log_130.change_message = u''
    django_admin_log_130 = save_or_locate(django_admin_log_130)

    django_admin_log_131 = LogEntry()
    django_admin_log_131.action_time = datetime.datetime(2013, 6, 11, 15, 22, 58, tzinfo=<UTC>)
    django_admin_log_131.user = auth_user_1
    django_admin_log_131.content_type = ContentType.objects.get(app_label="auth", model="user")
    django_admin_log_131.object_id = u'2'
    django_admin_log_131.object_repr = u'mschmier'
    django_admin_log_131.action_flag = 2
    django_admin_log_131.change_message = u'Changed password, first_name, last_name, email, is_staff and groups.'
    django_admin_log_131 = save_or_locate(django_admin_log_131)

    django_admin_log_132 = LogEntry()
    django_admin_log_132.action_time = datetime.datetime(2013, 6, 11, 15, 22, 28, tzinfo=<UTC>)
    django_admin_log_132.user = auth_user_1
    django_admin_log_132.content_type = ContentType.objects.get(app_label="auth", model="user")
    django_admin_log_132.object_id = u'2'
    django_admin_log_132.object_repr = u'mschmier'
    django_admin_log_132.action_flag = 1
    django_admin_log_132.change_message = u''
    django_admin_log_132 = save_or_locate(django_admin_log_132)

    django_admin_log_133 = LogEntry()
    django_admin_log_133.action_time = datetime.datetime(2013, 6, 11, 15, 22, 4, tzinfo=<UTC>)
    django_admin_log_133.user = auth_user_1
    django_admin_log_133.content_type = ContentType.objects.get(app_label="auth", model="group")
    django_admin_log_133.object_id = u'4'
    django_admin_log_133.object_repr = u'AP Admin'
    django_admin_log_133.action_flag = 1
    django_admin_log_133.change_message = u''
    django_admin_log_133 = save_or_locate(django_admin_log_133)

    django_admin_log_134 = LogEntry()
    django_admin_log_134.action_time = datetime.datetime(2013, 6, 11, 15, 21, 7, tzinfo=<UTC>)
    django_admin_log_134.user = auth_user_1
    django_admin_log_134.content_type = ContentType.objects.get(app_label="auth", model="group")
    django_admin_log_134.object_id = u'3'
    django_admin_log_134.object_repr = u'Posting'
    django_admin_log_134.action_flag = 2
    django_admin_log_134.change_message = u'Changed name and permissions.'
    django_admin_log_134 = save_or_locate(django_admin_log_134)

    django_admin_log_135 = LogEntry()
    django_admin_log_135.action_time = datetime.datetime(2013, 6, 11, 15, 20, 20, tzinfo=<UTC>)
    django_admin_log_135.user = auth_user_1
    django_admin_log_135.content_type = ContentType.objects.get(app_label="auth", model="group")
    django_admin_log_135.object_id = u'3'
    django_admin_log_135.object_repr = u'AP Admin'
    django_admin_log_135.action_flag = 1
    django_admin_log_135.change_message = u''
    django_admin_log_135 = save_or_locate(django_admin_log_135)

    django_admin_log_136 = LogEntry()
    django_admin_log_136.action_time = datetime.datetime(2013, 6, 11, 15, 18, 43, tzinfo=<UTC>)
    django_admin_log_136.user = auth_user_1
    django_admin_log_136.content_type = ContentType.objects.get(app_label="auth", model="group")
    django_admin_log_136.object_id = u'2'
    django_admin_log_136.object_repr = u'Rep Admin'
    django_admin_log_136.action_flag = 1
    django_admin_log_136.change_message = u''
    django_admin_log_136 = save_or_locate(django_admin_log_136)

    django_admin_log_137 = LogEntry()
    django_admin_log_137.action_time = datetime.datetime(2013, 6, 11, 15, 18, 32, tzinfo=<UTC>)
    django_admin_log_137.user = auth_user_1
    django_admin_log_137.content_type = ContentType.objects.get(app_label="auth", model="group")
    django_admin_log_137.object_id = u'1'
    django_admin_log_137.object_repr = u'Sales Rep'
    django_admin_log_137.action_flag = 2
    django_admin_log_137.change_message = u'Changed name.'
    django_admin_log_137 = save_or_locate(django_admin_log_137)

    django_admin_log_138 = LogEntry()
    django_admin_log_138.action_time = datetime.datetime(2013, 6, 11, 15, 15, 34, tzinfo=<UTC>)
    django_admin_log_138.user = auth_user_1
    django_admin_log_138.content_type = ContentType.objects.get(app_label="auth", model="group")
    django_admin_log_138.object_id = u'1'
    django_admin_log_138.object_repr = u'Rep Admin'
    django_admin_log_138.action_flag = 1
    django_admin_log_138.change_message = u''
    django_admin_log_138 = save_or_locate(django_admin_log_138)

    #Processing model: Category

    from tasks.models import Category

    tasks_category_1 = Category()
    tasks_category_1.description = u'At Home'
    tasks_category_1 = save_or_locate(tasks_category_1)

    tasks_category_2 = Category()
    tasks_category_2.description = u'In Pharmacy'
    tasks_category_2 = save_or_locate(tasks_category_2)

    tasks_category_3 = Category()
    tasks_category_3.description = u'Phone Call'
    tasks_category_3 = save_or_locate(tasks_category_3)

    tasks_category_4 = Category()
    tasks_category_4.description = u'Refills'
    tasks_category_4 = save_or_locate(tasks_category_4)

    tasks_category_5 = Category()
    tasks_category_5.description = u'Text Message'
    tasks_category_5 = save_or_locate(tasks_category_5)

    #Processing model: MultiPractice

    from practices.models import MultiPractice

    practices_multipractice_1 = MultiPractice()
    practices_multipractice_1.name = u'Schwartz Incorporated'
    practices_multipractice_1 = save_or_locate(practices_multipractice_1)

    practices_multipractice_2 = MultiPractice()
    practices_multipractice_2.name = u'Upper East Pain'
    practices_multipractice_2 = save_or_locate(practices_multipractice_2)

    #Processing model: Category

    from practices.models import Category

    practices_category_1 = Category()
    practices_category_1.description = u'Oncology'
    practices_category_1 = save_or_locate(practices_category_1)

    practices_category_2 = Category()
    practices_category_2.description = u'Pain'
    practices_category_2 = save_or_locate(practices_category_2)

    practices_category_3 = Category()
    practices_category_3.description = u'Rheumatology'
    practices_category_3 = save_or_locate(practices_category_3)

    #Processing model: ContactType

    from practices.models import ContactType

    practices_contacttype_1 = ContactType()
    practices_contacttype_1.description = u'Nurse'
    practices_contacttype_1 = save_or_locate(practices_contacttype_1)

    practices_contacttype_2 = ContactType()
    practices_contacttype_2.description = u'Office Manager'
    practices_contacttype_2 = save_or_locate(practices_contacttype_2)

    practices_contacttype_3 = ContactType()
    practices_contacttype_3.description = u'Other'
    practices_contacttype_3 = save_or_locate(practices_contacttype_3)

    practices_contacttype_4 = ContactType()
    practices_contacttype_4.description = u'Receptionist'
    practices_contacttype_4 = save_or_locate(practices_contacttype_4)

    #Processing model: CommissionTag

    from salesreps.models import CommissionTag

    salesreps_commissiontag_1 = CommissionTag()
    salesreps_commissiontag_1.tag = u'BB'
    salesreps_commissiontag_1 = save_or_locate(salesreps_commissiontag_1)

    salesreps_commissiontag_2 = CommissionTag()
    salesreps_commissiontag_2.tag = u'BP'
    salesreps_commissiontag_2 = save_or_locate(salesreps_commissiontag_2)

    salesreps_commissiontag_3 = CommissionTag()
    salesreps_commissiontag_3.tag = u'FB'
    salesreps_commissiontag_3 = save_or_locate(salesreps_commissiontag_3)

    salesreps_commissiontag_4 = CommissionTag()
    salesreps_commissiontag_4.tag = u'PB'
    salesreps_commissiontag_4 = save_or_locate(salesreps_commissiontag_4)

    #Processing model: CommissionTagSplit

    from salesreps.models import CommissionTagSplit

    salesreps_commissiontagsplit_1 = CommissionTagSplit()
    salesreps_commissiontagsplit_1.sales_rep = auth_user_3
    salesreps_commissiontagsplit_1.commission_tag = salesreps_commissiontag_1
    salesreps_commissiontagsplit_1.commission_percent = 0.015
    salesreps_commissiontagsplit_1.is_inactive = False
    salesreps_commissiontagsplit_1 = save_or_locate(salesreps_commissiontagsplit_1)

    salesreps_commissiontagsplit_2 = CommissionTagSplit()
    salesreps_commissiontagsplit_2.sales_rep = auth_user_3
    salesreps_commissiontagsplit_2.commission_tag = salesreps_commissiontag_3
    salesreps_commissiontagsplit_2.commission_percent = 0.0075
    salesreps_commissiontagsplit_2.is_inactive = False
    salesreps_commissiontagsplit_2 = save_or_locate(salesreps_commissiontagsplit_2)

    salesreps_commissiontagsplit_3 = CommissionTagSplit()
    salesreps_commissiontagsplit_3.sales_rep = auth_user_3
    salesreps_commissiontagsplit_3.commission_tag = salesreps_commissiontag_2
    salesreps_commissiontagsplit_3.commission_percent = 0.0075
    salesreps_commissiontagsplit_3.is_inactive = False
    salesreps_commissiontagsplit_3 = save_or_locate(salesreps_commissiontagsplit_3)

    salesreps_commissiontagsplit_4 = CommissionTagSplit()
    salesreps_commissiontagsplit_4.sales_rep = auth_user_6
    salesreps_commissiontagsplit_4.commission_tag = salesreps_commissiontag_2
    salesreps_commissiontagsplit_4.commission_percent = 0.0075
    salesreps_commissiontagsplit_4.is_inactive = False
    salesreps_commissiontagsplit_4 = save_or_locate(salesreps_commissiontagsplit_4)

    salesreps_commissiontagsplit_5 = CommissionTagSplit()
    salesreps_commissiontagsplit_5.sales_rep = auth_user_6
    salesreps_commissiontagsplit_5.commission_tag = salesreps_commissiontag_2
    salesreps_commissiontagsplit_5.commission_percent = 0.0075
    salesreps_commissiontagsplit_5.is_inactive = False
    salesreps_commissiontagsplit_5 = save_or_locate(salesreps_commissiontagsplit_5)

    #Processing model: DrugCompany

    from drugcompanies.models import DrugCompany

    drugcompanies_drugcompany_1 = DrugCompany()
    drugcompanies_drugcompany_1.name = u'Teva'
    drugcompanies_drugcompany_1 = save_or_locate(drugcompanies_drugcompany_1)

    #Processing model: Drug

    from drugcompanies.models import Drug

    drugcompanies_drug_1 = Drug()
    drugcompanies_drug_1.name = u'Fentora'
    drugcompanies_drug_1.is_brand = False
    drugcompanies_drug_1 = save_or_locate(drugcompanies_drug_1)

    drugcompanies_drug_2 = Drug()
    drugcompanies_drug_2.name = u'Amrix'
    drugcompanies_drug_2.is_brand = True
    drugcompanies_drug_2 = save_or_locate(drugcompanies_drug_2)

    #Processing model: DrugNDC

    from drugcompanies.models import DrugNDC

    drugcompanies_drugndc_1 = DrugNDC()
    drugcompanies_drugndc_1.opus_key = 0
    drugcompanies_drugndc_1.name = u'Fentora'
    drugcompanies_drugndc_1.drug = drugcompanies_drug_1
    drugcompanies_drugndc_1.ndc = u'039485309'
    drugcompanies_drugndc_1.strength = 60
    drugcompanies_drugndc_1.strength_units = u'mg'
    drugcompanies_drugndc_1 = save_or_locate(drugcompanies_drugndc_1)

    drugcompanies_drugndc_2 = DrugNDC()
    drugcompanies_drugndc_2.opus_key = 1
    drugcompanies_drugndc_2.name = u'Fentora'
    drugcompanies_drugndc_2.drug = drugcompanies_drug_1
    drugcompanies_drugndc_2.ndc = u'4053909453'
    drugcompanies_drugndc_2.strength = 100
    drugcompanies_drugndc_2.strength_units = u'mg'
    drugcompanies_drugndc_2 = save_or_locate(drugcompanies_drugndc_2)

    drugcompanies_drugndc_3 = DrugNDC()
    drugcompanies_drugndc_3.opus_key = 3
    drugcompanies_drugndc_3.name = u'Amrix'
    drugcompanies_drugndc_3.drug = drugcompanies_drug_2
    drugcompanies_drugndc_3.ndc = u'408535738453'
    drugcompanies_drugndc_3.strength = 50
    drugcompanies_drugndc_3.strength_units = u'mg'
    drugcompanies_drugndc_3 = save_or_locate(drugcompanies_drugndc_3)

    #Processing model: Division

    from drugcompanies.models import Division

    drugcompanies_division_1 = Division()
    drugcompanies_division_1.name = u'Pain'
    drugcompanies_division_1.company = drugcompanies_drugcompany_1
    drugcompanies_division_1 = save_or_locate(drugcompanies_division_1)

    drugcompanies_division_1.drug.add(drugcompanies_drug_1)
    drugcompanies_division_1.drug.add(drugcompanies_drug_2)

    #Processing model: Manager

    from drugcompanies.models import Manager

    drugcompanies_manager_1 = Manager()
    drugcompanies_manager_1.first_name = u'John'
    drugcompanies_manager_1.last_name = u'Harold'
    drugcompanies_manager_1.email = u'john.harold@tevapharm.com'
    drugcompanies_manager_1.is_inactive = False
    drugcompanies_manager_1.comment = u'2/6/13 - Met him at Atlantic Grill lunch w/ Glenn and Marc Oseroff.  Went great, he loved the idea of linden care.  He will be at managers dinner 2/12/13.   He prefers text message for communication'
    drugcompanies_manager_1.division = drugcompanies_division_1
    drugcompanies_manager_1.territory = u'Massachussetts'
    drugcompanies_manager_1 = save_or_locate(drugcompanies_manager_1)

    #Processing model: DrugRep

    from drugcompanies.models import DrugRep

    drugcompanies_drugrep_1 = DrugRep()
    drugcompanies_drugrep_1.first_name = u'Lindsay'
    drugcompanies_drugrep_1.last_name = u'Klein'
    drugcompanies_drugrep_1.email = u''
    drugcompanies_drugrep_1.is_inactive = False
    drugcompanies_drugrep_1.comment = u''
    drugcompanies_drugrep_1.manager = drugcompanies_manager_1
    drugcompanies_drugrep_1.regions = u''
    drugcompanies_drugrep_1 = save_or_locate(drugcompanies_drugrep_1)

    drugcompanies_drugrep_2 = DrugRep()
    drugcompanies_drugrep_2.first_name = u'Mike'
    drugcompanies_drugrep_2.last_name = u'Judge'
    drugcompanies_drugrep_2.email = u'mikeJ@gmail.com'
    drugcompanies_drugrep_2.is_inactive = False
    drugcompanies_drugrep_2.comment = u''
    drugcompanies_drugrep_2.manager = drugcompanies_manager_1
    drugcompanies_drugrep_2.regions = u''
    drugcompanies_drugrep_2 = save_or_locate(drugcompanies_drugrep_2)

    #Processing model: Patient

    from patients.models import Patient

    patients_patient_1 = Patient()
    patients_patient_1.first_name = u'Craig'
    patients_patient_1.last_name = u'Cohen'
    patients_patient_1.email = u''
    patients_patient_1.is_inactive = False
    patients_patient_1.comment = u''
    patients_patient_1.address = u''
    patients_patient_1.address2 = u''
    patients_patient_1.city = u''
    patients_patient_1.state = u''
    patients_patient_1.zip_code = u''
    patients_patient_1.opus_key = 0
    patients_patient_1.commission_tag = salesreps_commissiontag_1
    patients_patient_1 = save_or_locate(patients_patient_1)

    patients_patient_2 = Patient()
    patients_patient_2.first_name = u'Scott'
    patients_patient_2.last_name = u'Meltzer'
    patients_patient_2.email = u''
    patients_patient_2.is_inactive = False
    patients_patient_2.comment = u''
    patients_patient_2.address = u''
    patients_patient_2.address2 = u''
    patients_patient_2.city = u''
    patients_patient_2.state = u''
    patients_patient_2.zip_code = u''
    patients_patient_2.opus_key = 0
    patients_patient_2.commission_tag = salesreps_commissiontag_3
    patients_patient_2 = save_or_locate(patients_patient_2)

    patients_patient_3 = Patient()
    patients_patient_3.first_name = u'Monica'
    patients_patient_3.last_name = u'Samuel'
    patients_patient_3.email = u''
    patients_patient_3.is_inactive = False
    patients_patient_3.comment = u''
    patients_patient_3.address = u''
    patients_patient_3.address2 = u''
    patients_patient_3.city = u''
    patients_patient_3.state = u''
    patients_patient_3.zip_code = u''
    patients_patient_3.opus_key = 0
    patients_patient_3.commission_tag = None
    patients_patient_3 = save_or_locate(patients_patient_3)

    #Processing model: Batch

    from payments.models import Batch

    payments_batch_1 = Batch()
    payments_batch_1.code = u'062513A'
    payments_batch_1.amount = Decimal('34093.32')
    payments_batch_1.date_deposited = datetime.date(2013, 6, 27)
    payments_batch_1.date_added = datetime.date(2013, 6, 25)
    payments_batch_1 = save_or_locate(payments_batch_1)

    payments_batch_2 = Batch()
    payments_batch_2.code = u'062313A'
    payments_batch_2.amount = Decimal('531.32')
    payments_batch_2.date_deposited = datetime.date(2013, 6, 14)
    payments_batch_2.date_added = datetime.date(2013, 6, 23)
    payments_batch_2 = save_or_locate(payments_batch_2)

    #Processing model: PaymentType

    from payments.models import PaymentType

    payments_paymenttype_1 = PaymentType()
    payments_paymenttype_1.name = u'835'
    payments_paymenttype_1 = save_or_locate(payments_paymenttype_1)

    payments_paymenttype_2 = PaymentType()
    payments_paymenttype_2.name = u'Manual'
    payments_paymenttype_2 = save_or_locate(payments_paymenttype_2)

    payments_paymenttype_3 = PaymentType()
    payments_paymenttype_3.name = u'Write Down'
    payments_paymenttype_3 = save_or_locate(payments_paymenttype_3)

    payments_paymenttype_4 = PaymentType()
    payments_paymenttype_4.name = u'Upload'
    payments_paymenttype_4 = save_or_locate(payments_paymenttype_4)

    payments_paymenttype_5 = PaymentType()
    payments_paymenttype_5.name = u'E-Voucher Upload'
    payments_paymenttype_5 = save_or_locate(payments_paymenttype_5)

    #Processing model: Region

    from regions.models import Region

    regions_region_1 = Region()
    regions_region_1.name = u'Alabama'
    regions_region_1 = save_or_locate(regions_region_1)

    regions_region_2 = Region()
    regions_region_2.name = u'Arkansas'
    regions_region_2 = save_or_locate(regions_region_2)

    regions_region_3 = Region()
    regions_region_3.name = u'Bronx'
    regions_region_3 = save_or_locate(regions_region_3)

    regions_region_4 = Region()
    regions_region_4.name = u'Brooklyn'
    regions_region_4 = save_or_locate(regions_region_4)

    regions_region_5 = Region()
    regions_region_5.name = u'Colorado'
    regions_region_5 = save_or_locate(regions_region_5)

    regions_region_6 = Region()
    regions_region_6.name = u'Connecticut'
    regions_region_6 = save_or_locate(regions_region_6)

    regions_region_7 = Region()
    regions_region_7.name = u'Deleware'
    regions_region_7 = save_or_locate(regions_region_7)

    regions_region_8 = Region()
    regions_region_8.name = u'Florida'
    regions_region_8 = save_or_locate(regions_region_8)

    regions_region_9 = Region()
    regions_region_9.name = u'Georgia'
    regions_region_9 = save_or_locate(regions_region_9)

    regions_region_10 = Region()
    regions_region_10.name = u'Illinois'
    regions_region_10 = save_or_locate(regions_region_10)

    regions_region_11 = Region()
    regions_region_11.name = u'Indiana'
    regions_region_11 = save_or_locate(regions_region_11)

    regions_region_12 = Region()
    regions_region_12.name = u'Kentucky'
    regions_region_12 = save_or_locate(regions_region_12)

    regions_region_13 = Region()
    regions_region_13.name = u'Long Island'
    regions_region_13 = save_or_locate(regions_region_13)

    regions_region_14 = Region()
    regions_region_14.name = u'Louisiana'
    regions_region_14 = save_or_locate(regions_region_14)

    regions_region_15 = Region()
    regions_region_15.name = u'Manhattan'
    regions_region_15 = save_or_locate(regions_region_15)

    regions_region_16 = Region()
    regions_region_16.name = u'Maryland'
    regions_region_16 = save_or_locate(regions_region_16)

    regions_region_17 = Region()
    regions_region_17.name = u'Massachusetts'
    regions_region_17 = save_or_locate(regions_region_17)

    regions_region_18 = Region()
    regions_region_18.name = u'Michigan'
    regions_region_18 = save_or_locate(regions_region_18)

    regions_region_19 = Region()
    regions_region_19.name = u'New Jersey'
    regions_region_19 = save_or_locate(regions_region_19)

    regions_region_20 = Region()
    regions_region_20.name = u'North Carolina'
    regions_region_20 = save_or_locate(regions_region_20)

    regions_region_21 = Region()
    regions_region_21.name = u'Ohio'
    regions_region_21 = save_or_locate(regions_region_21)

    regions_region_22 = Region()
    regions_region_22.name = u'Queens'
    regions_region_22 = save_or_locate(regions_region_22)

    regions_region_23 = Region()
    regions_region_23.name = u'Upstate New York'
    regions_region_23 = save_or_locate(regions_region_23)

    regions_region_24 = Region()
    regions_region_24.name = u'Wisconsin'
    regions_region_24 = save_or_locate(regions_region_24)

    #Processing model: SubRegion

    from regions.models import SubRegion

    regions_subregion_1 = SubRegion()
    regions_subregion_1.name = u'South Jersey'
    regions_subregion_1.region = regions_region_19
    regions_subregion_1 = save_or_locate(regions_subregion_1)

    regions_subregion_2 = SubRegion()
    regions_subregion_2.name = u'North Jersey'
    regions_subregion_2.region = regions_region_19
    regions_subregion_2 = save_or_locate(regions_subregion_2)

    regions_subregion_3 = SubRegion()
    regions_subregion_3.name = u'Upper East Side'
    regions_subregion_3.region = regions_region_15
    regions_subregion_3 = save_or_locate(regions_subregion_3)

    regions_subregion_4 = SubRegion()
    regions_subregion_4.name = u'Lower East Side'
    regions_subregion_4.region = regions_region_15
    regions_subregion_4 = save_or_locate(regions_subregion_4)

    regions_subregion_5 = SubRegion()
    regions_subregion_5.name = u'Midtown'
    regions_subregion_5.region = regions_region_15
    regions_subregion_5 = save_or_locate(regions_subregion_5)

    regions_subregion_6 = SubRegion()
    regions_subregion_6.name = u'Lower West Side'
    regions_subregion_6.region = regions_region_15
    regions_subregion_6 = save_or_locate(regions_subregion_6)

    regions_subregion_7 = SubRegion()
    regions_subregion_7.name = u'Upper West Side'
    regions_subregion_7.region = regions_region_15
    regions_subregion_7 = save_or_locate(regions_subregion_7)

    regions_subregion_8 = SubRegion()
    regions_subregion_8.name = u'Syracuse'
    regions_subregion_8.region = regions_region_23
    regions_subregion_8 = save_or_locate(regions_subregion_8)

    regions_subregion_9 = SubRegion()
    regions_subregion_9.name = u'Buffalo'
    regions_subregion_9.region = regions_region_15
    regions_subregion_9 = save_or_locate(regions_subregion_9)

    regions_subregion_10 = SubRegion()
    regions_subregion_10.name = u'Nassau County'
    regions_subregion_10.region = regions_region_15
    regions_subregion_10 = save_or_locate(regions_subregion_10)

    regions_subregion_11 = SubRegion()
    regions_subregion_11.name = u'Suffolk County'
    regions_subregion_11.region = regions_region_15
    regions_subregion_11 = save_or_locate(regions_subregion_11)

    #Processing model: Payor

    from insurance.models import Payor

    insurance_payor_1 = Payor()
    insurance_payor_1.name = u'Caremark'
    insurance_payor_1 = save_or_locate(insurance_payor_1)

    insurance_payor_2 = Payor()
    insurance_payor_2.name = u'Express Scripts'
    insurance_payor_2 = save_or_locate(insurance_payor_2)

    insurance_payor_3 = Payor()
    insurance_payor_3.name = u'Medco'
    insurance_payor_3 = save_or_locate(insurance_payor_3)

    #Processing model: BinNumber

    from insurance.models import BinNumber

    insurance_binnumber_1 = BinNumber()
    insurance_binnumber_1.bin_number = 123456
    insurance_binnumber_1.payor = insurance_payor_1
    insurance_binnumber_1 = save_or_locate(insurance_binnumber_1)

    insurance_binnumber_2 = BinNumber()
    insurance_binnumber_2.bin_number = 544443
    insurance_binnumber_2.payor = insurance_payor_3
    insurance_binnumber_2 = save_or_locate(insurance_binnumber_2)

    #Processing model: Insuror

    from insurance.models import Insuror

    insurance_insuror_1 = Insuror()
    insurance_insuror_1.carrier_code = u'PD'
    insurance_insuror_1.plan_code = u''
    insurance_insuror_1.bin_number = insurance_binnumber_1
    insurance_insuror_1 = save_or_locate(insurance_insuror_1)

    insurance_insuror_2 = Insuror()
    insurance_insuror_2.carrier_code = u'MC'
    insurance_insuror_2.plan_code = u'J9999'
    insurance_insuror_2.bin_number = insurance_binnumber_1
    insurance_insuror_2 = save_or_locate(insurance_insuror_2)

    insurance_insuror_3 = Insuror()
    insurance_insuror_3.carrier_code = u'AL'
    insurance_insuror_3.plan_code = u''
    insurance_insuror_3.bin_number = insurance_binnumber_2
    insurance_insuror_3 = save_or_locate(insurance_insuror_3)

    #Processing model: InteractionType

    from interactions.models import InteractionType

    interactions_interactiontype_1 = InteractionType()
    interactions_interactiontype_1.name = u'Phone Call'
    interactions_interactiontype_1 = save_or_locate(interactions_interactiontype_1)

    interactions_interactiontype_2 = InteractionType()
    interactions_interactiontype_2.name = u'E-mail'
    interactions_interactiontype_2 = save_or_locate(interactions_interactiontype_2)

    interactions_interactiontype_3 = InteractionType()
    interactions_interactiontype_3.name = u'Text Message'
    interactions_interactiontype_3 = save_or_locate(interactions_interactiontype_3)

    #Processing model: Interaction

    from interactions.models import Interaction


    #Processing model: Practice

    from practices.models import Practice

    practices_practice_1 = Practice()
    practices_practice_1.address = u''
    practices_practice_1.address2 = u''
    practices_practice_1.city = u''
    practices_practice_1.state = u''
    practices_practice_1.zip_code = u''
    practices_practice_1.name = u'Fake Practice'
    practices_practice_1.multi_practice = None
    practices_practice_1.ideal_visits = 2
    practices_practice_1.potential = 10000.0
    practices_practice_1.is_inactive = False
    practices_practice_1.comment = u''
    practices_practice_1.next_visit = u''
    practices_practice_1.sub_region = None
    practices_practice_1 = save_or_locate(practices_practice_1)

    practices_practice_2 = Practice()
    practices_practice_2.address = u''
    practices_practice_2.address2 = u''
    practices_practice_2.city = u''
    practices_practice_2.state = u''
    practices_practice_2.zip_code = u''
    practices_practice_2.name = u'Another Practice'
    practices_practice_2.multi_practice = None
    practices_practice_2.ideal_visits = 1
    practices_practice_2.potential = 2000.0
    practices_practice_2.is_inactive = True
    practices_practice_2.comment = u''
    practices_practice_2.next_visit = u''
    practices_practice_2.sub_region = None
    practices_practice_2 = save_or_locate(practices_practice_2)

    practices_practice_3 = Practice()
    practices_practice_3.address = u''
    practices_practice_3.address2 = u''
    practices_practice_3.city = u''
    practices_practice_3.state = u''
    practices_practice_3.zip_code = u''
    practices_practice_3.name = u"Craig's Practice"
    practices_practice_3.multi_practice = None
    practices_practice_3.ideal_visits = 0
    practices_practice_3.potential = None
    practices_practice_3.is_inactive = False
    practices_practice_3.comment = u''
    practices_practice_3.next_visit = u''
    practices_practice_3.sub_region = None
    practices_practice_3 = save_or_locate(practices_practice_3)

    practices_practice_4 = Practice()
    practices_practice_4.address = u''
    practices_practice_4.address2 = u''
    practices_practice_4.city = u''
    practices_practice_4.state = u''
    practices_practice_4.zip_code = u''
    practices_practice_4.name = u'Douglas Schwartz East'
    practices_practice_4.multi_practice = practices_multipractice_1
    practices_practice_4.ideal_visits = 0
    practices_practice_4.potential = 2000.0
    practices_practice_4.is_inactive = False
    practices_practice_4.comment = u'Mondays are best'
    practices_practice_4.next_visit = u'Bring fruit basket'
    practices_practice_4.sub_region = None
    practices_practice_4 = save_or_locate(practices_practice_4)

    practices_practice_4.category.add(practices_category_2)
    practices_practice_4.drug_rep.add(drugcompanies_drugrep_2)

    practices_practice_5 = Practice()
    practices_practice_5.address = u''
    practices_practice_5.address2 = u''
    practices_practice_5.city = u''
    practices_practice_5.state = u''
    practices_practice_5.zip_code = u''
    practices_practice_5.name = u'Douglas Schwartz West'
    practices_practice_5.multi_practice = practices_multipractice_1
    practices_practice_5.ideal_visits = 0
    practices_practice_5.potential = None
    practices_practice_5.is_inactive = False
    practices_practice_5.comment = u''
    practices_practice_5.next_visit = u''
    practices_practice_5.sub_region = None
    practices_practice_5 = save_or_locate(practices_practice_5)

    practices_practice_5.category.add(practices_category_3)
    practices_practice_5.drug_rep.add(drugcompanies_drugrep_1)

    #Processing model: Doctor

    from practices.models import Doctor

    practices_doctor_1 = Doctor()
    practices_doctor_1.first_name = u'Craig'
    practices_doctor_1.last_name = u'Cohen'
    practices_doctor_1.email = u''
    practices_doctor_1.is_inactive = False
    practices_doctor_1.comment = u''
    practices_doctor_1.practice = practices_practice_1
    practices_doctor_1.opus_key = 1
    practices_doctor_1.commission_tag = None
    practices_doctor_1 = save_or_locate(practices_doctor_1)

    practices_doctor_2 = Doctor()
    practices_doctor_2.first_name = u'Douglas'
    practices_doctor_2.last_name = u'Schwartz'
    practices_doctor_2.email = u'doug@schwartz.edu'
    practices_doctor_2.is_inactive = False
    practices_doctor_2.comment = u''
    practices_doctor_2.practice = practices_practice_4
    practices_doctor_2.opus_key = 0
    practices_doctor_2.commission_tag = None
    practices_doctor_2 = save_or_locate(practices_doctor_2)

    practices_doctor_3 = Doctor()
    practices_doctor_3.first_name = u'John'
    practices_doctor_3.last_name = u'Doe'
    practices_doctor_3.email = u''
    practices_doctor_3.is_inactive = False
    practices_doctor_3.comment = u''
    practices_doctor_3.practice = practices_practice_4
    practices_doctor_3.opus_key = 100
    practices_doctor_3.commission_tag = None
    practices_doctor_3 = save_or_locate(practices_doctor_3)

    practices_doctor_4 = Doctor()
    practices_doctor_4.first_name = u'Lebron'
    practices_doctor_4.last_name = u'James'
    practices_doctor_4.email = u''
    practices_doctor_4.is_inactive = False
    practices_doctor_4.comment = u''
    practices_doctor_4.practice = practices_practice_5
    practices_doctor_4.opus_key = 1001
    practices_doctor_4.commission_tag = None
    practices_doctor_4 = save_or_locate(practices_doctor_4)

    #Processing model: PracticeContact

    from practices.models import PracticeContact

    practices_practicecontact_1 = PracticeContact()
    practices_practicecontact_1.first_name = u'Lisa'
    practices_practicecontact_1.last_name = u'Hochberger'
    practices_practicecontact_1.email = u''
    practices_practicecontact_1.is_inactive = False
    practices_practicecontact_1.comment = u''
    practices_practicecontact_1.practice = practices_practice_4
    practices_practicecontact_1.contact_type = practices_contacttype_2
    practices_practicecontact_1 = save_or_locate(practices_practicecontact_1)

    practices_practicecontact_2 = PracticeContact()
    practices_practicecontact_2.first_name = u'Jill'
    practices_practicecontact_2.last_name = u'Marx'
    practices_practicecontact_2.email = u''
    practices_practicecontact_2.is_inactive = False
    practices_practicecontact_2.comment = u''
    practices_practicecontact_2.practice = practices_practice_3
    practices_practicecontact_2.contact_type = practices_contacttype_1
    practices_practicecontact_2 = save_or_locate(practices_practicecontact_2)

    #Processing model: Appointment

    from appointments.models import Appointment

    appointments_appointment_1 = Appointment()
    appointments_appointment_1.practice = practices_practice_2
    appointments_appointment_1.visit_date = datetime.datetime(2013, 6, 24, 4, 47, 43, tzinfo=<UTC>)
    appointments_appointment_1.comment = u'go to there'
    appointments_appointment_1.is_complete = False
    appointments_appointment_1.sales_rep = auth_user_6
    appointments_appointment_1 = save_or_locate(appointments_appointment_1)

    appointments_appointment_2 = Appointment()
    appointments_appointment_2.practice = practices_practice_1
    appointments_appointment_2.visit_date = datetime.datetime(2013, 6, 23, 4, 48, 35, tzinfo=<UTC>)
    appointments_appointment_2.comment = u''
    appointments_appointment_2.is_complete = True
    appointments_appointment_2.sales_rep = auth_user_1
    appointments_appointment_2 = save_or_locate(appointments_appointment_2)

    appointments_appointment_3 = Appointment()
    appointments_appointment_3.practice = practices_practice_3
    appointments_appointment_3.visit_date = datetime.datetime(2013, 6, 23, 5, 6, 29, tzinfo=<UTC>)
    appointments_appointment_3.comment = u''
    appointments_appointment_3.is_complete = False
    appointments_appointment_3.sales_rep = auth_user_3
    appointments_appointment_3 = save_or_locate(appointments_appointment_3)

    appointments_appointment_4 = Appointment()
    appointments_appointment_4.practice = practices_practice_1
    appointments_appointment_4.visit_date = datetime.datetime(2013, 6, 23, 5, 7, 8, tzinfo=<UTC>)
    appointments_appointment_4.comment = u''
    appointments_appointment_4.is_complete = False
    appointments_appointment_4.sales_rep = auth_user_6
    appointments_appointment_4 = save_or_locate(appointments_appointment_4)

    #Processing model: Check

    from payments.models import Check

    payments_check_1 = Check()
    payments_check_1.check_number = u'000523452'
    payments_check_1.payor = insurance_payor_1
    payments_check_1.date = datetime.date(2013, 6, 25)
    payments_check_1.date_deposited = datetime.date(2013, 6, 27)
    payments_check_1.amount = Decimal('3453.33')
    payments_check_1.fee = Decimal('0.00')
    payments_check_1.batch = payments_batch_1
    payments_check_1 = save_or_locate(payments_check_1)

    payments_check_2 = Check()
    payments_check_2.check_number = u'46744673'
    payments_check_2.payor = insurance_payor_1
    payments_check_2.date = datetime.date(2013, 6, 25)
    payments_check_2.date_deposited = datetime.date(2013, 6, 23)
    payments_check_2.amount = Decimal('345.22')
    payments_check_2.fee = Decimal('1.56')
    payments_check_2.batch = payments_batch_2
    payments_check_2 = save_or_locate(payments_check_2)

    #Processing model: Script

    from prescriptions.models import Script

    prescriptions_script_1 = Script()
    prescriptions_script_1.opus_key = 1
    prescriptions_script_1.script_number = 425333
    prescriptions_script_1.refill_number = 0
    prescriptions_script_1.date_of_service = datetime.date(2013, 6, 25)
    prescriptions_script_1.deleted_date = datetime.date(2013, 6, 25)
    prescriptions_script_1.drug_ndc = drugcompanies_drugndc_1
    prescriptions_script_1.patient = patients_patient_1
    prescriptions_script_1.commission_tag = salesreps_commissiontag_1
    prescriptions_script_1.acquisition_price = Decimal('342.32')
    prescriptions_script_1.doctor = practices_doctor_2
    prescriptions_script_1.third_party_script = 1
    prescriptions_script_1.is_filled_by_robot = False
    prescriptions_script_1.last_cash_posting_date = datetime.date(2013, 6, 25)
    prescriptions_script_1.is_non_processed = False
    prescriptions_script_1 = save_or_locate(prescriptions_script_1)

    prescriptions_script_2 = Script()
    prescriptions_script_2.opus_key = 1
    prescriptions_script_2.script_number = 345322
    prescriptions_script_2.refill_number = 1
    prescriptions_script_2.date_of_service = datetime.date(2013, 6, 19)
    prescriptions_script_2.deleted_date = datetime.date(2013, 6, 21)
    prescriptions_script_2.drug_ndc = drugcompanies_drugndc_3
    prescriptions_script_2.patient = patients_patient_3
    prescriptions_script_2.commission_tag = salesreps_commissiontag_3
    prescriptions_script_2.acquisition_price = Decimal('23.23')
    prescriptions_script_2.doctor = practices_doctor_4
    prescriptions_script_2.third_party_script = 2
    prescriptions_script_2.is_filled_by_robot = False
    prescriptions_script_2.last_cash_posting_date = datetime.date(2013, 6, 25)
    prescriptions_script_2.is_non_processed = False
    prescriptions_script_2 = save_or_locate(prescriptions_script_2)

    #Processing model: ScriptTransaction

    from prescriptions.models import ScriptTransaction

    prescriptions_scripttransaction_1 = ScriptTransaction()
    prescriptions_scripttransaction_1.opus_key = 1
    prescriptions_scripttransaction_1.opus_table = u''
    prescriptions_scripttransaction_1.transaction_date = datetime.date(2013, 6, 25)
    prescriptions_scripttransaction_1.insuror = insurance_insuror_1
    prescriptions_scripttransaction_1.payor_order = 1
    prescriptions_scripttransaction_1.is_non_processed = False
    prescriptions_scripttransaction_1.deleted_date = datetime.date(2013, 6, 25)
    prescriptions_scripttransaction_1.amount = Decimal('657.33')
    prescriptions_scripttransaction_1 = save_or_locate(prescriptions_scripttransaction_1)

    prescriptions_scripttransaction_2 = ScriptTransaction()
    prescriptions_scripttransaction_2.opus_key = 1
    prescriptions_scripttransaction_2.opus_table = u''
    prescriptions_scripttransaction_2.transaction_date = datetime.date(2013, 6, 25)
    prescriptions_scripttransaction_2.insuror = insurance_insuror_2
    prescriptions_scripttransaction_2.payor_order = 2
    prescriptions_scripttransaction_2.is_non_processed = False
    prescriptions_scripttransaction_2.deleted_date = datetime.date(2013, 6, 25)
    prescriptions_scripttransaction_2.amount = Decimal('3457.32')
    prescriptions_scripttransaction_2 = save_or_locate(prescriptions_scripttransaction_2)

    prescriptions_scripttransaction_3 = ScriptTransaction()
    prescriptions_scripttransaction_3.opus_key = 4
    prescriptions_scripttransaction_3.opus_table = u''
    prescriptions_scripttransaction_3.transaction_date = datetime.date(2013, 6, 24)
    prescriptions_scripttransaction_3.insuror = insurance_insuror_3
    prescriptions_scripttransaction_3.payor_order = 1
    prescriptions_scripttransaction_3.is_non_processed = False
    prescriptions_scripttransaction_3.deleted_date = datetime.date(2013, 6, 25)
    prescriptions_scripttransaction_3.amount = Decimal('341.56')
    prescriptions_scripttransaction_3 = save_or_locate(prescriptions_scripttransaction_3)

    #Processing model: Task

    from tasks.models import Task

    tasks_task_1 = Task()
    tasks_task_1.task_date = datetime.datetime(2013, 6, 26, 4, 2, 28, tzinfo=<UTC>)
    tasks_task_1.description = u'Go to bank'
    tasks_task_1.is_completed = False
    tasks_task_1.is_in_schedule = False
    tasks_task_1.practice = None
    tasks_task_1.category = None
    tasks_task_1.urgency = u'low'
    tasks_task_1.sales_rep = auth_user_3
    tasks_task_1 = save_or_locate(tasks_task_1)

    tasks_task_2 = Task()
    tasks_task_2.task_date = datetime.datetime(2013, 6, 26, 4, 2, 28, tzinfo=<UTC>)
    tasks_task_2.description = u'Script 380222'
    tasks_task_2.is_completed = False
    tasks_task_2.is_in_schedule = False
    tasks_task_2.practice = None
    tasks_task_2.category = tasks_category_4
    tasks_task_2.urgency = u'medium'
    tasks_task_2.sales_rep = auth_user_6
    tasks_task_2 = save_or_locate(tasks_task_2)

    tasks_task_3 = Task()
    tasks_task_3.task_date = datetime.datetime(2013, 6, 26, 4, 2, 28, tzinfo=<UTC>)
    tasks_task_3.description = u'Call Fentora Rep'
    tasks_task_3.is_completed = False
    tasks_task_3.is_in_schedule = False
    tasks_task_3.practice = None
    tasks_task_3.category = practices_category_2
    tasks_task_3.urgency = u'high'
    tasks_task_3.sales_rep = auth_user_3
    tasks_task_3 = save_or_locate(tasks_task_3)

    #Processing model: PaymentTransaction

    from payments.models import PaymentTransaction

    payments_paymenttransaction_1 = PaymentTransaction()
    payments_paymenttransaction_1.script_transaction = prescriptions_scripttransaction_1
    payments_paymenttransaction_1.check = payments_check_1
    payments_paymenttransaction_1.amount = Decimal('657.33')
    payments_paymenttransaction_1.payment_type = payments_paymenttype_1
    payments_paymenttransaction_1.date_received = datetime.date(2013, 6, 26)
    payments_paymenttransaction_1.date_added = datetime.date(2013, 6, 26)
    payments_paymenttransaction_1 = save_or_locate(payments_paymenttransaction_1)

    payments_paymenttransaction_2 = PaymentTransaction()
    payments_paymenttransaction_2.script_transaction = prescriptions_scripttransaction_2
    payments_paymenttransaction_2.check = payments_check_1
    payments_paymenttransaction_2.amount = Decimal('3000.00')
    payments_paymenttransaction_2.payment_type = payments_paymenttype_2
    payments_paymenttransaction_2.date_received = datetime.date(2013, 6, 26)
    payments_paymenttransaction_2.date_added = datetime.date(2013, 6, 26)
    payments_paymenttransaction_2 = save_or_locate(payments_paymenttransaction_2)

