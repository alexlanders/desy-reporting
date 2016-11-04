# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models



class CourseInstructors(models.Model):
    course_instructors_item_id = models.AutoField(primary_key=True)
    course_id = models.IntegerField()
    instructor_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'course_instructors'


class Courses(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_start_date = models.DateField()
    course_end_date = models.DateField()
    organization_id = models.IntegerField()
    course_notes = models.TextField()

    class Meta:
        managed = False
        db_table = 'courses'


class DriveTemplateBehaviors(models.Model):
    drive_template_behavior_id = models.AutoField(primary_key=True)
    drive_template_id = models.IntegerField()
    standard_drive_behavior_id = models.IntegerField()
    drive_template_objective_id = models.IntegerField()
    drive_template_behavior_sequence_order = models.IntegerField()
    drive_template_behavior_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drive_template_behaviors'


class DriveTemplateObjectives(models.Model):
    drive_template_objective_id = models.AutoField(primary_key=True)
    drive_template_id = models.IntegerField()
    standard_drive_objective_id = models.IntegerField()
    drive_template_objective_sequence_order = models.IntegerField()
    drive_template_objective_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drive_template_objectives'


class DriveTemplates(models.Model):
    drive_template_id = models.AutoField(primary_key=True)
    drive_template_sequence_order = models.IntegerField()
    drive_template_organization_id = models.IntegerField()
    drive_template_duration = models.FloatField()
    drive_template_notes = models.TextField(blank=True, null=True)
    drive_template_description = models.TextField()

    class Meta:
        managed = False
        db_table = 'drive_templates'


class EngineCost(models.Model):
    engine_name = models.CharField(max_length=64)
    device_type = models.IntegerField()
    cost_name = models.CharField(max_length=64)
    cost_value = models.FloatField(blank=True, null=True)
    last_update = models.DateTimeField()
    comment = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engine_cost'
        unique_together = (('cost_name', 'engine_name', 'device_type'),)


class Event(models.Model):
    db = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    body = models.TextField()
    definer = models.CharField(max_length=93)
    execute_at = models.DateTimeField(blank=True, null=True)
    interval_value = models.IntegerField(blank=True, null=True)
    interval_field = models.CharField(max_length=18, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    last_executed = models.DateTimeField(blank=True, null=True)
    starts = models.DateTimeField(blank=True, null=True)
    ends = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=18)
    on_completion = models.CharField(max_length=8)
    sql_mode = models.CharField(max_length=478)
    comment = models.CharField(max_length=64)
    originator = models.IntegerField()
    time_zone = models.CharField(max_length=64)
    character_set_client = models.CharField(max_length=32, blank=True, null=True)
    collation_connection = models.CharField(max_length=32, blank=True, null=True)
    db_collation = models.CharField(max_length=32, blank=True, null=True)
    body_utf8 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event'
        unique_together = (('db', 'name'),)


class FinalDriveBehaviors(models.Model):
    final_drive_behavior_id = models.AutoField(primary_key=True)
    final_drive_id = models.IntegerField()
    final_drive_behavior_deduction = models.IntegerField(blank=True, null=True)
    final_drive_template_behavior_id = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'final_drive_behaviors'


class FinalDriveManeuvers(models.Model):
    final_drive_maneuver_id = models.AutoField(primary_key=True)
    final_drive_template_maneuver_id = models.IntegerField()
    final_drive_id = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'final_drive_maneuvers'


class FinalDriveStandardBehaviors(models.Model):
    final_drive_standard_behavior_id = models.AutoField(primary_key=True)
    final_drive_standard_behavior_description = models.TextField()
    standard_drive_behavior_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'final_drive_standard_behaviors'


class FinalDriveStandardManeuverBehaviorSets(models.Model):
    final_drive_standard_maneuver_behavior_set_id = models.AutoField(primary_key=True)
    final_drive_standard_maneuver_id = models.IntegerField()
    final_drive_standard_behavior_id = models.IntegerField()
    final_drive_standard_behavior_sequence_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'final_drive_standard_maneuver_behavior_sets'


class FinalDriveStandardManeuverSubtypes(models.Model):
    final_drive_standard_maneuver_subtype_id = models.AutoField(primary_key=True)
    final_drive_standard_maneuver_subtype = models.TextField()
    final_drive_standard_maneuver_subtype_notes = models.TextField(blank=True, null=True)
    final_drive_standard_maneuver_type_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'final_drive_standard_maneuver_subtypes'


class FinalDriveStandardManeuverTypes(models.Model):
    final_drive_standard_maneuver_type_id = models.AutoField(primary_key=True)
    final_drive_standard_maneuver_type = models.TextField()
    final_drive_standard_maneuver_type_notes = models.TextField(blank=True, null=True)
    final_drive_standard_maneuver_required = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'final_drive_standard_maneuver_types'


class FinalDriveStandardManeuvers(models.Model):
    final_drive_standard_maneuver_id = models.AutoField(primary_key=True)
    final_drive_standard_maneuver_type_id = models.IntegerField()
    final_drive_standard_maneuver_subtype_id = models.IntegerField(blank=True, null=True)
    final_drive_standard_maneuver_description = models.TextField()
    final_drive_standard_maneuver_notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'final_drive_standard_maneuvers'


class FinalDriveTemplateBehaviors(models.Model):
    final_drive_template_behavior_id = models.AutoField(primary_key=True)
    final_drive_template_maneuver_id = models.IntegerField()
    final_drive_template_behavior_sequence_order = models.IntegerField()
    final_drive_template_behavior_description = models.TextField()
    final_drive_standard_behavior_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'final_drive_template_behaviors'


class FinalDriveTemplateManeuvers(models.Model):
    final_drive_template_maneuver_id = models.AutoField(primary_key=True)
    final_drive_template_alternate_maneuver_description = models.TextField(blank=True, null=True)
    final_drive_template_id = models.IntegerField()
    final_drive_template_maneuver_location = models.TextField(blank=True, null=True)
    final_drive_template_maneuver_notes = models.TextField(blank=True, null=True)
    final_drive_template_maneuver_sequence_order = models.IntegerField()
    final_drive_standard_maneuver_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'final_drive_template_maneuvers'


class FinalDriveTemplates(models.Model):
    final_drive_template_id = models.AutoField(primary_key=True)
    organization_id = models.IntegerField()
    final_drive_template_duration = models.DecimalField(max_digits=10, decimal_places=0)
    final_drive_template_notes = models.TextField(blank=True, null=True)
    final_drive_template_description = models.TextField()

    class Meta:
        managed = False
        db_table = 'final_drive_templates'


class FinalDrives(models.Model):
    final_drive_id = models.AutoField(primary_key=True)
    student_id = models.IntegerField()
    course_id = models.IntegerField()
    has_corrective_lenses = models.IntegerField(blank=True, null=True)
    has_permit = models.IntegerField(blank=True, null=True)
    instructor_id = models.IntegerField()
    final_drive_date = models.DateField(blank=True, null=True)
    final_drive_student_signature = models.TextField(blank=True, null=True)
    gif_code = models.IntegerField(blank=True, null=True)
    final_drive_instructor_signature = models.TextField(blank=True, null=True)
    final_drive_total_deductions = models.DecimalField(max_digits=10, decimal_places=0)
    final_drive_total_score = models.TextField(blank=True, null=True)
    final_drive_template_id = models.IntegerField()
    final_drive_comments = models.TextField(blank=True, null=True)
    final_drive_hours_driven = models.FloatField(blank=True, null=True)
    final_drive_hours_observed = models.FloatField(blank=True, null=True)
    final_drive_status = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'final_drives'


class Func(models.Model):
    name = models.CharField(primary_key=True, max_length=64)
    ret = models.IntegerField()
    dl = models.CharField(max_length=128)
    type = models.CharField(max_length=9)

    class Meta:
        managed = False
        db_table = 'func'


class GeneralLog(models.Model):
    event_time = models.DateTimeField()
    user_host = models.TextField()
    thread_id = models.BigIntegerField()
    server_id = models.IntegerField()
    command_type = models.CharField(max_length=64)
    argument = models.TextField()

    class Meta:
        managed = False
        db_table = 'general_log'


class GtidExecuted(models.Model):
    source_uuid = models.CharField(max_length=36)
    interval_start = models.BigIntegerField()
    interval_end = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'gtid_executed'
        unique_together = (('source_uuid', 'interval_start'),)


class HelpCategory(models.Model):
    help_category_id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)
    parent_category_id = models.SmallIntegerField(blank=True, null=True)
    url = models.TextField()

    class Meta:
        managed = False
        db_table = 'help_category'


class HelpKeyword(models.Model):
    help_keyword_id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'help_keyword'


class HelpRelation(models.Model):
    help_topic_id = models.IntegerField()
    help_keyword_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'help_relation'
        unique_together = (('help_keyword_id', 'help_topic_id'),)


class HelpTopic(models.Model):
    help_topic_id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)
    help_category_id = models.SmallIntegerField()
    description = models.TextField()
    example = models.TextField()
    url = models.TextField()

    class Meta:
        managed = False
        db_table = 'help_topic'


class InnodbIndexStats(models.Model):
    database_name = models.CharField(max_length=64)
    table_name = models.CharField(max_length=64)
    index_name = models.CharField(max_length=64)
    last_update = models.DateTimeField()
    stat_name = models.CharField(max_length=64)
    stat_value = models.BigIntegerField()
    sample_size = models.BigIntegerField(blank=True, null=True)
    stat_description = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'innodb_index_stats'
        unique_together = (('database_name', 'table_name', 'index_name', 'stat_name'),)


class InnodbTableStats(models.Model):
    database_name = models.CharField(max_length=64)
    table_name = models.CharField(max_length=64)
    last_update = models.DateTimeField()
    n_rows = models.BigIntegerField()
    clustered_index_size = models.BigIntegerField()
    sum_of_other_index_sizes = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'innodb_table_stats'
        unique_together = (('database_name', 'table_name'),)


class NdbBinlogIndex(models.Model):
    position = models.BigIntegerField(db_column='Position')  # Field name made lowercase.
    file = models.CharField(db_column='File', max_length=255)  # Field name made lowercase.
    epoch = models.BigIntegerField()
    inserts = models.IntegerField()
    updates = models.IntegerField()
    deletes = models.IntegerField()
    schemaops = models.IntegerField()
    orig_server_id = models.IntegerField()
    orig_epoch = models.BigIntegerField()
    gci = models.IntegerField()
    next_position = models.BigIntegerField()
    next_file = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ndb_binlog_index'
        unique_together = (('epoch', 'orig_server_id', 'orig_epoch'),)


class OrganizationAffiliations(models.Model):
    organization_affiliation_id = models.AutoField(primary_key=True)
    person_id = models.IntegerField()
    organization_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'organization_affiliations'


class OrganizationTypes(models.Model):
    organization_type_id = models.AutoField(primary_key=True)
    organization_type = models.CharField(max_length=30)
    organization_type_comment = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'organization_types'


class Organizations(models.Model):
    organization_id = models.AutoField(primary_key=True)
    organization_name = models.CharField(max_length=100)
    organization_address1 = models.CharField(max_length=100)
    organization_address2 = models.CharField(max_length=100)
    organization_city = models.CharField(max_length=50)
    organization_state = models.CharField(max_length=2)
    organization_zip = models.CharField(db_column='organization_ZIP', max_length=5)  # Field name made lowercase.
    organization_phone = models.CharField(max_length=20)
    organization_primary_contact_id = models.IntegerField()
    organization_secondary_contact_id = models.IntegerField()
    organization_type = models.CharField(max_length=50)
    organization_logo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organizations'


class People(models.Model):
    person_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=10)
    middle_initial = models.CharField(max_length=1, blank=True, null=True)
    last_name = models.CharField(max_length=20)
    address1 = models.CharField(max_length=40)
    address2 = models.CharField(max_length=40, blank=True, null=True)
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=2)
    zip = models.CharField(db_column='ZIP', max_length=5)  # Field name made lowercase.
    mobile_phone = models.CharField(max_length=20)
    home_phone = models.CharField(max_length=20, blank=True, null=True)
    business_phone = models.CharField(max_length=20, blank=True, null=True)
    email1 = models.CharField(max_length=40)
    email2 = models.CharField(max_length=40, blank=True, null=True)
    person_type = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'people'


class PersonTypes(models.Model):
    person_type_id = models.AutoField(primary_key=True)
    person_type_name = models.CharField(max_length=50)
    security_class_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'person_types'


class Plugin(models.Model):
    name = models.CharField(primary_key=True, max_length=64)
    dl = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'plugin'


class Proc(models.Model):
    db = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=9)
    specific_name = models.CharField(max_length=64)
    language = models.CharField(max_length=3)
    sql_data_access = models.CharField(max_length=17)
    is_deterministic = models.CharField(max_length=3)
    security_type = models.CharField(max_length=7)
    param_list = models.TextField()
    returns = models.TextField()
    body = models.TextField()
    definer = models.CharField(max_length=93)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    sql_mode = models.CharField(max_length=478)
    comment = models.TextField()
    character_set_client = models.CharField(max_length=32, blank=True, null=True)
    collation_connection = models.CharField(max_length=32, blank=True, null=True)
    db_collation = models.CharField(max_length=32, blank=True, null=True)
    body_utf8 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proc'
        unique_together = (('db', 'name', 'type'),)


class ProcsPriv(models.Model):
    host = models.CharField(db_column='Host', max_length=60)  # Field name made lowercase.
    db = models.CharField(db_column='Db', max_length=64)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=32)  # Field name made lowercase.
    routine_name = models.CharField(db_column='Routine_name', max_length=64)  # Field name made lowercase.
    routine_type = models.CharField(db_column='Routine_type', max_length=9)  # Field name made lowercase.
    grantor = models.CharField(db_column='Grantor', max_length=93)  # Field name made lowercase.
    proc_priv = models.CharField(db_column='Proc_priv', max_length=27)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'procs_priv'
        unique_together = (('host', 'db', 'user', 'routine_name', 'routine_type'),)


class ProxiesPriv(models.Model):
    host = models.CharField(db_column='Host', max_length=60)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=32)  # Field name made lowercase.
    proxied_host = models.CharField(db_column='Proxied_host', max_length=60)  # Field name made lowercase.
    proxied_user = models.CharField(db_column='Proxied_user', max_length=32)  # Field name made lowercase.
    with_grant = models.IntegerField(db_column='With_grant')  # Field name made lowercase.
    grantor = models.CharField(db_column='Grantor', max_length=93)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proxies_priv'
        unique_together = (('host', 'user', 'proxied_host', 'proxied_user'),)


class Rubric(models.Model):
    rubric_item_id = models.AutoField(primary_key=True)
    rubric_item_sequence_order = models.IntegerField()
    rubric_item_points = models.IntegerField()
    rubric_item_description = models.TextField()

    class Meta:
        managed = False
        db_table = 'rubric'


class SecurityClasses(models.Model):
    security_class_id = models.AutoField(primary_key=True)
    security_class_name = models.CharField(max_length=40)
    security_class_comments = models.TextField()

    class Meta:
        managed = False
        db_table = 'security_classes'


class SecurityQuestions(models.Model):
    security_question_id = models.AutoField(primary_key=True)
    login_id = models.IntegerField()
    security_question = models.TextField()
    question_answer = models.TextField()

    class Meta:
        managed = False
        db_table = 'security_questions'


class ServerCost(models.Model):
    cost_name = models.CharField(primary_key=True, max_length=64)
    cost_value = models.FloatField(blank=True, null=True)
    last_update = models.DateTimeField()
    comment = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'server_cost'


class Servers(models.Model):
    server_name = models.CharField(db_column='Server_name', primary_key=True, max_length=64)  # Field name made lowercase.
    host = models.CharField(db_column='Host', max_length=64)  # Field name made lowercase.
    db = models.CharField(db_column='Db', max_length=64)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=64)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=64)  # Field name made lowercase.
    port = models.IntegerField(db_column='Port')  # Field name made lowercase.
    socket = models.CharField(db_column='Socket', max_length=64)  # Field name made lowercase.
    wrapper = models.CharField(db_column='Wrapper', max_length=64)  # Field name made lowercase.
    owner = models.CharField(db_column='Owner', max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'servers'


class Sessions(models.Model):
    session_id = models.CharField(primary_key=True, max_length=40)
    login_id = models.IntegerField()
    ip_address = models.CharField(max_length=45, blank=True, null=True)
    session_start = models.DateTimeField()
    last_activity = models.IntegerField(blank=True, null=True)
    session_expired = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sessions'


class SlaveMasterInfo(models.Model):
    number_of_lines = models.IntegerField(db_column='Number_of_lines')  # Field name made lowercase.
    master_log_name = models.TextField(db_column='Master_log_name')  # Field name made lowercase.
    master_log_pos = models.BigIntegerField(db_column='Master_log_pos')  # Field name made lowercase.
    host = models.CharField(db_column='Host', max_length=64, blank=True, null=True)  # Field name made lowercase.
    user_name = models.TextField(db_column='User_name', blank=True, null=True)  # Field name made lowercase.
    user_password = models.TextField(db_column='User_password', blank=True, null=True)  # Field name made lowercase.
    port = models.IntegerField(db_column='Port')  # Field name made lowercase.
    connect_retry = models.IntegerField(db_column='Connect_retry')  # Field name made lowercase.
    enabled_ssl = models.IntegerField(db_column='Enabled_ssl')  # Field name made lowercase.
    ssl_ca = models.TextField(db_column='Ssl_ca', blank=True, null=True)  # Field name made lowercase.
    ssl_capath = models.TextField(db_column='Ssl_capath', blank=True, null=True)  # Field name made lowercase.
    ssl_cert = models.TextField(db_column='Ssl_cert', blank=True, null=True)  # Field name made lowercase.
    ssl_cipher = models.TextField(db_column='Ssl_cipher', blank=True, null=True)  # Field name made lowercase.
    ssl_key = models.TextField(db_column='Ssl_key', blank=True, null=True)  # Field name made lowercase.
    ssl_verify_server_cert = models.IntegerField(db_column='Ssl_verify_server_cert')  # Field name made lowercase.
    heartbeat = models.FloatField(db_column='Heartbeat')  # Field name made lowercase.
    bind = models.TextField(db_column='Bind', blank=True, null=True)  # Field name made lowercase.
    ignored_server_ids = models.TextField(db_column='Ignored_server_ids', blank=True, null=True)  # Field name made lowercase.
    uuid = models.TextField(db_column='Uuid', blank=True, null=True)  # Field name made lowercase.
    retry_count = models.BigIntegerField(db_column='Retry_count')  # Field name made lowercase.
    ssl_crl = models.TextField(db_column='Ssl_crl', blank=True, null=True)  # Field name made lowercase.
    ssl_crlpath = models.TextField(db_column='Ssl_crlpath', blank=True, null=True)  # Field name made lowercase.
    enabled_auto_position = models.IntegerField(db_column='Enabled_auto_position')  # Field name made lowercase.
    channel_name = models.CharField(db_column='Channel_name', primary_key=True, max_length=64)  # Field name made lowercase.
    tls_version = models.TextField(db_column='Tls_version', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'slave_master_info'


class SlaveRelayLogInfo(models.Model):
    number_of_lines = models.IntegerField(db_column='Number_of_lines')  # Field name made lowercase.
    relay_log_name = models.TextField(db_column='Relay_log_name')  # Field name made lowercase.
    relay_log_pos = models.BigIntegerField(db_column='Relay_log_pos')  # Field name made lowercase.
    master_log_name = models.TextField(db_column='Master_log_name')  # Field name made lowercase.
    master_log_pos = models.BigIntegerField(db_column='Master_log_pos')  # Field name made lowercase.
    sql_delay = models.IntegerField(db_column='Sql_delay')  # Field name made lowercase.
    number_of_workers = models.IntegerField(db_column='Number_of_workers')  # Field name made lowercase.
    id = models.IntegerField(db_column='Id')  # Field name made lowercase.
    channel_name = models.CharField(db_column='Channel_name', primary_key=True, max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'slave_relay_log_info'


class SlaveWorkerInfo(models.Model):
    id = models.IntegerField(db_column='Id')  # Field name made lowercase.
    relay_log_name = models.TextField(db_column='Relay_log_name')  # Field name made lowercase.
    relay_log_pos = models.BigIntegerField(db_column='Relay_log_pos')  # Field name made lowercase.
    master_log_name = models.TextField(db_column='Master_log_name')  # Field name made lowercase.
    master_log_pos = models.BigIntegerField(db_column='Master_log_pos')  # Field name made lowercase.
    checkpoint_relay_log_name = models.TextField(db_column='Checkpoint_relay_log_name')  # Field name made lowercase.
    checkpoint_relay_log_pos = models.BigIntegerField(db_column='Checkpoint_relay_log_pos')  # Field name made lowercase.
    checkpoint_master_log_name = models.TextField(db_column='Checkpoint_master_log_name')  # Field name made lowercase.
    checkpoint_master_log_pos = models.BigIntegerField(db_column='Checkpoint_master_log_pos')  # Field name made lowercase.
    checkpoint_seqno = models.IntegerField(db_column='Checkpoint_seqno')  # Field name made lowercase.
    checkpoint_group_size = models.IntegerField(db_column='Checkpoint_group_size')  # Field name made lowercase.
    checkpoint_group_bitmap = models.TextField(db_column='Checkpoint_group_bitmap')  # Field name made lowercase.
    channel_name = models.CharField(db_column='Channel_name', max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'slave_worker_info'
        unique_together = (('channel_name', 'id'),)


class SlowLog(models.Model):
    start_time = models.DateTimeField()
    user_host = models.TextField()
    query_time = models.TimeField()
    lock_time = models.TimeField()
    rows_sent = models.IntegerField()
    rows_examined = models.IntegerField()
    db = models.CharField(max_length=512)
    last_insert_id = models.IntegerField()
    insert_id = models.IntegerField()
    server_id = models.IntegerField()
    sql_text = models.TextField()
    thread_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'slow_log'


class StandardDriveBehaviors(models.Model):
    standard_drive_behavior_id = models.AutoField(primary_key=True)
    standard_drive_behavior_name = models.TextField()
    standard_drive_behavior_notes = models.TextField()
    standard_drive_chapter = models.IntegerField()
    standard_drive_objective_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'standard_drive_behaviors'


class StandardDriveGroups(models.Model):
    standard_drive_group_id = models.AutoField(primary_key=True)
    standard_drive_group_description = models.TextField()
    standard_drive_group_notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'standard_drive_groups'


class StandardDriveObjectives(models.Model):
    standard_drive_objective_id = models.AutoField(primary_key=True)
    standard_drive_objective_name = models.CharField(max_length=100)
    standard_drive_objective_notes = models.TextField()
    playbook_chapter = models.IntegerField()
    standard_drive_objective_code = models.CharField(max_length=10)
    standard_drive_group_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'standard_drive_objectives'


class States(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=50)
    state_abbreviation = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'states'


class StudentDriveBehaviors(models.Model):
    student_drive_behavior_id = models.AutoField(primary_key=True)
    student_drive_behavior_score = models.IntegerField(blank=True, null=True)
    student_drive_id = models.IntegerField()
    standard_drive_behavior_id = models.IntegerField()
    drive_template_behavior_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'student_drive_behaviors'


class StudentDriveObjectives(models.Model):
    student_drive_objective_id = models.AutoField(primary_key=True)
    standard_drive_objective_id = models.IntegerField()
    student_drive_id = models.IntegerField()
    drive_template_objective_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'student_drive_objectives'


class StudentDrives(models.Model):
    student_drive_id = models.AutoField(primary_key=True)
    course_id = models.IntegerField()
    student_id = models.IntegerField()
    instructor_id = models.IntegerField(blank=True, null=True)
    drive_date = models.DateField(blank=True, null=True)
    has_corrective_lenses = models.IntegerField(blank=True, null=True)
    has_permit = models.IntegerField(blank=True, null=True)
    parent_signature = models.IntegerField(blank=True, null=True)
    parent_signature_date = models.DateField(blank=True, null=True)
    parent_signature_id = models.IntegerField(blank=True, null=True)
    student_drive_comments = models.TextField(blank=True, null=True)
    drive_template_id = models.IntegerField()
    total_score = models.IntegerField(blank=True, null=True)
    parent_practice_hours = models.FloatField(blank=True, null=True)
    parent_behaviors_practiced = models.TextField(blank=True, null=True)
    student_drive_hours_driven = models.FloatField(blank=True, null=True)
    student_drive_hours_observed = models.FloatField(blank=True, null=True)
    student_drive_status = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_drives'


class StudentInfo(models.Model):
    student = models.ForeignKey(People, models.DO_NOTHING, primary_key=True)
    person_id = models.IntegerField()
    permit_number = models.CharField(max_length=10)
    corrective_lenses = models.IntegerField()
    parent1_id = models.IntegerField()
    parent2_id = models.IntegerField(blank=True, null=True)
    total_hours_driven = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    total_hours_observed = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    total_parent_practice_hours = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_info'


class TablesPriv(models.Model):
    host = models.CharField(db_column='Host', max_length=60)  # Field name made lowercase.
    db = models.CharField(db_column='Db', max_length=64)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=32)  # Field name made lowercase.
    table_name = models.CharField(db_column='Table_name', max_length=64)  # Field name made lowercase.
    grantor = models.CharField(db_column='Grantor', max_length=93)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp')  # Field name made lowercase.
    table_priv = models.CharField(db_column='Table_priv', max_length=98)  # Field name made lowercase.
    column_priv = models.CharField(db_column='Column_priv', max_length=31)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tables_priv'
        unique_together = (('host', 'db', 'user', 'table_name'),)


class TimeZone(models.Model):
    time_zone_id = models.AutoField(db_column='Time_zone_id', primary_key=True)  # Field name made lowercase.
    use_leap_seconds = models.CharField(db_column='Use_leap_seconds', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'time_zone'


class TimeZoneLeapSecond(models.Model):
    transition_time = models.BigIntegerField(db_column='Transition_time', primary_key=True)  # Field name made lowercase.
    correction = models.IntegerField(db_column='Correction')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'time_zone_leap_second'


class TimeZoneName(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=64)  # Field name made lowercase.
    time_zone_id = models.IntegerField(db_column='Time_zone_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'time_zone_name'


class TimeZoneTransition(models.Model):
    time_zone_id = models.IntegerField(db_column='Time_zone_id')  # Field name made lowercase.
    transition_time = models.BigIntegerField(db_column='Transition_time')  # Field name made lowercase.
    transition_type_id = models.IntegerField(db_column='Transition_type_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'time_zone_transition'
        unique_together = (('time_zone_id', 'transition_time'),)


class TimeZoneTransitionType(models.Model):
    time_zone_id = models.IntegerField(db_column='Time_zone_id')  # Field name made lowercase.
    transition_type_id = models.IntegerField(db_column='Transition_type_id')  # Field name made lowercase.
    offset = models.IntegerField(db_column='Offset')  # Field name made lowercase.
    is_dst = models.IntegerField(db_column='Is_DST')  # Field name made lowercase.
    abbreviation = models.CharField(db_column='Abbreviation', max_length=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'time_zone_transition_type'
        unique_together = (('time_zone_id', 'transition_type_id'),)


class User(models.Model):
    host = models.CharField(db_column='Host', max_length=60)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=32)  # Field name made lowercase.
    select_priv = models.CharField(db_column='Select_priv', max_length=1)  # Field name made lowercase.
    insert_priv = models.CharField(db_column='Insert_priv', max_length=1)  # Field name made lowercase.
    update_priv = models.CharField(db_column='Update_priv', max_length=1)  # Field name made lowercase.
    delete_priv = models.CharField(db_column='Delete_priv', max_length=1)  # Field name made lowercase.
    create_priv = models.CharField(db_column='Create_priv', max_length=1)  # Field name made lowercase.
    drop_priv = models.CharField(db_column='Drop_priv', max_length=1)  # Field name made lowercase.
    reload_priv = models.CharField(db_column='Reload_priv', max_length=1)  # Field name made lowercase.
    shutdown_priv = models.CharField(db_column='Shutdown_priv', max_length=1)  # Field name made lowercase.
    process_priv = models.CharField(db_column='Process_priv', max_length=1)  # Field name made lowercase.
    file_priv = models.CharField(db_column='File_priv', max_length=1)  # Field name made lowercase.
    grant_priv = models.CharField(db_column='Grant_priv', max_length=1)  # Field name made lowercase.
    references_priv = models.CharField(db_column='References_priv', max_length=1)  # Field name made lowercase.
    index_priv = models.CharField(db_column='Index_priv', max_length=1)  # Field name made lowercase.
    alter_priv = models.CharField(db_column='Alter_priv', max_length=1)  # Field name made lowercase.
    show_db_priv = models.CharField(db_column='Show_db_priv', max_length=1)  # Field name made lowercase.
    super_priv = models.CharField(db_column='Super_priv', max_length=1)  # Field name made lowercase.
    create_tmp_table_priv = models.CharField(db_column='Create_tmp_table_priv', max_length=1)  # Field name made lowercase.
    lock_tables_priv = models.CharField(db_column='Lock_tables_priv', max_length=1)  # Field name made lowercase.
    execute_priv = models.CharField(db_column='Execute_priv', max_length=1)  # Field name made lowercase.
    repl_slave_priv = models.CharField(db_column='Repl_slave_priv', max_length=1)  # Field name made lowercase.
    repl_client_priv = models.CharField(db_column='Repl_client_priv', max_length=1)  # Field name made lowercase.
    create_view_priv = models.CharField(db_column='Create_view_priv', max_length=1)  # Field name made lowercase.
    show_view_priv = models.CharField(db_column='Show_view_priv', max_length=1)  # Field name made lowercase.
    create_routine_priv = models.CharField(db_column='Create_routine_priv', max_length=1)  # Field name made lowercase.
    alter_routine_priv = models.CharField(db_column='Alter_routine_priv', max_length=1)  # Field name made lowercase.
    create_user_priv = models.CharField(db_column='Create_user_priv', max_length=1)  # Field name made lowercase.
    event_priv = models.CharField(db_column='Event_priv', max_length=1)  # Field name made lowercase.
    trigger_priv = models.CharField(db_column='Trigger_priv', max_length=1)  # Field name made lowercase.
    create_tablespace_priv = models.CharField(db_column='Create_tablespace_priv', max_length=1)  # Field name made lowercase.
    ssl_type = models.CharField(max_length=9)
    ssl_cipher = models.TextField()
    x509_issuer = models.TextField()
    x509_subject = models.TextField()
    max_questions = models.IntegerField()
    max_updates = models.IntegerField()
    max_connections = models.IntegerField()
    max_user_connections = models.IntegerField()
    plugin = models.CharField(max_length=64)
    authentication_string = models.TextField(blank=True, null=True)
    password_expired = models.CharField(max_length=1)
    password_last_changed = models.DateTimeField(blank=True, null=True)
    password_lifetime = models.SmallIntegerField(blank=True, null=True)
    account_locked = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'user'
        unique_together = (('host', 'user'),)


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=30)
    hashed_password = models.CharField(max_length=100)
    salt = models.CharField(max_length=36)
    person_id = models.IntegerField()
    password_last_updated = models.DateTimeField()
    security_class = models.IntegerField(blank=True, null=True)
    first_login = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Vehicles(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    organization_id = models.IntegerField()
    registration_number = models.CharField(max_length=10)
    vehicle_make = models.CharField(max_length=10)
    vehicle_body_type = models.CharField(max_length=10)
    license_number = models.CharField(max_length=10)
    vin = models.CharField(db_column='VIN', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vehicles'
