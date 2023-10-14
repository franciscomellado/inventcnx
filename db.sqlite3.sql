BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
	"id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_user_groups" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_admin_log" (
	"id"	integer NOT NULL,
	"object_id"	text,
	"object_repr"	varchar(200) NOT NULL,
	"action_flag"	smallint unsigned NOT NULL CHECK("action_flag" >= 0),
	"change_message"	text NOT NULL,
	"content_type_id"	integer,
	"user_id"	integer NOT NULL,
	"action_time"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_content_type" (
	"id"	integer NOT NULL,
	"app_label"	varchar(100) NOT NULL,
	"model"	varchar(100) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_permission" (
	"id"	integer NOT NULL,
	"content_type_id"	integer NOT NULL,
	"codename"	varchar(100) NOT NULL,
	"name"	varchar(255) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_group" (
	"id"	integer NOT NULL,
	"name"	varchar(150) NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_user" (
	"id"	integer NOT NULL,
	"password"	varchar(128) NOT NULL,
	"last_login"	datetime,
	"is_superuser"	bool NOT NULL,
	"username"	varchar(150) NOT NULL UNIQUE,
	"last_name"	varchar(150) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"is_staff"	bool NOT NULL,
	"is_active"	bool NOT NULL,
	"date_joined"	datetime NOT NULL,
	"first_name"	varchar(150) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "personas_area" (
	"id"	integer NOT NULL,
	"nombre"	varchar(100) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "personas_departamento" (
	"id"	integer NOT NULL,
	"nombre"	varchar(100) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "personas_personas" (
	"id"	integer NOT NULL,
	"nombre"	varchar(100) NOT NULL,
	"apellido"	varchar(100) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"area_id"	bigint NOT NULL,
	"departamento_id"	bigint NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("area_id") REFERENCES "personas_area"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("departamento_id") REFERENCES "personas_departamento"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_session" (
	"session_key"	varchar(40) NOT NULL,
	"session_data"	text NOT NULL,
	"expire_date"	datetime NOT NULL,
	PRIMARY KEY("session_key")
);
CREATE TABLE IF NOT EXISTS "personas_prestamo" (
	"id"	integer NOT NULL,
	"fecha_prestamo"	datetime NOT NULL,
	"fecha_devolucion"	datetime NOT NULL,
	"nombre_id"	bigint NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("nombre_id") REFERENCES "personas_personas"("id") DEFERRABLE INITIALLY DEFERRED
);
INSERT INTO "django_migrations" VALUES (1,'contenttypes','0001_initial','2023-10-10 00:26:42.244261');
INSERT INTO "django_migrations" VALUES (2,'auth','0001_initial','2023-10-10 00:26:42.366065');
INSERT INTO "django_migrations" VALUES (3,'admin','0001_initial','2023-10-10 00:26:42.425068');
INSERT INTO "django_migrations" VALUES (4,'admin','0002_logentry_remove_auto_add','2023-10-10 00:26:42.528074');
INSERT INTO "django_migrations" VALUES (5,'admin','0003_logentry_add_action_flag_choices','2023-10-10 00:26:42.574077');
INSERT INTO "django_migrations" VALUES (6,'contenttypes','0002_remove_content_type_name','2023-10-10 00:26:42.656082');
INSERT INTO "django_migrations" VALUES (7,'auth','0002_alter_permission_name_max_length','2023-10-10 00:26:42.714085');
INSERT INTO "django_migrations" VALUES (8,'auth','0003_alter_user_email_max_length','2023-10-10 00:26:42.774088');
INSERT INTO "django_migrations" VALUES (9,'auth','0004_alter_user_username_opts','2023-10-10 00:26:42.840092');
INSERT INTO "django_migrations" VALUES (10,'auth','0005_alter_user_last_login_null','2023-10-10 00:26:42.895095');
INSERT INTO "django_migrations" VALUES (11,'auth','0006_require_contenttypes_0002','2023-10-10 00:26:42.970100');
INSERT INTO "django_migrations" VALUES (12,'auth','0007_alter_validators_add_error_messages','2023-10-10 00:26:43.014102');
INSERT INTO "django_migrations" VALUES (13,'auth','0008_alter_user_username_max_length','2023-10-10 00:26:43.080106');
INSERT INTO "django_migrations" VALUES (14,'auth','0009_alter_user_last_name_max_length','2023-10-10 00:26:43.142109');
INSERT INTO "django_migrations" VALUES (15,'auth','0010_alter_group_name_max_length','2023-10-10 00:26:43.235115');
INSERT INTO "django_migrations" VALUES (16,'auth','0011_update_proxy_permissions','2023-10-10 00:26:43.282117');
INSERT INTO "django_migrations" VALUES (17,'auth','0012_alter_user_first_name_max_length','2023-10-10 00:26:43.326120');
INSERT INTO "django_migrations" VALUES (18,'personas','0001_initial','2023-10-10 00:26:43.380123');
INSERT INTO "django_migrations" VALUES (19,'sessions','0001_initial','2023-10-10 00:26:43.423125');
INSERT INTO "django_migrations" VALUES (20,'personas','0002_rename_usuario_personas','2023-10-10 17:19:46.280370');
INSERT INTO "django_migrations" VALUES (21,'personas','0003_alter_personas_options','2023-10-11 05:26:20.877508');
INSERT INTO "django_admin_log" VALUES (1,'2','jdcadenas',1,'[{"added": {}}]',4,1,'2023-10-10 03:58:30.302701');
INSERT INTO "django_admin_log" VALUES (2,'2','jdcadenas',2,'[{"changed": {"fields": ["First name", "Last name", "Email address", "Staff status"]}}]',4,1,'2023-10-10 03:59:04.227485');
INSERT INTO "django_admin_log" VALUES (3,'3','usuarioprueba',2,'[{"changed": {"fields": ["First name", "Last name", "Staff status"]}}]',4,1,'2023-10-10 05:38:18.930792');
INSERT INTO "django_admin_log" VALUES (4,'1','Departamento object (1)',1,'[{"added": {}}]',8,1,'2023-10-10 21:27:51.357662');
INSERT INTO "django_admin_log" VALUES (5,'2','Departamento object (2)',1,'[{"added": {}}]',8,1,'2023-10-10 21:27:57.770029');
INSERT INTO "django_admin_log" VALUES (6,'3','Departamento object (3)',1,'[{"added": {}}]',8,1,'2023-10-10 21:28:07.211569');
INSERT INTO "django_admin_log" VALUES (7,'1','Area object (1)',1,'[{"added": {}}]',7,1,'2023-10-10 21:28:28.937811');
INSERT INTO "django_admin_log" VALUES (8,'2','Area object (2)',1,'[{"added": {}}]',7,1,'2023-10-10 21:28:33.614079');
INSERT INTO "django_admin_log" VALUES (9,'3','Area object (3)',1,'[{"added": {}}]',7,1,'2023-10-10 21:28:38.551361');
INSERT INTO "django_admin_log" VALUES (10,'1','Eum Rem beatae',1,'[{"added": {}}]',9,1,'2023-10-10 21:39:15.055942');
INSERT INTO "django_admin_log" VALUES (11,'4','area 5',1,'[{"added": {}}]',7,1,'2023-10-11 04:14:54.230172');
INSERT INTO "django_admin_log" VALUES (12,'4','Laudantium elit deleniti impedit officia amet magni quaerat quidem In earum sed proident cum non sed vel',2,'[{"changed": {"fields": ["Area"]}}]',9,1,'2023-10-11 04:15:11.544163');
INSERT INTO "django_content_type" VALUES (1,'admin','logentry');
INSERT INTO "django_content_type" VALUES (2,'auth','permission');
INSERT INTO "django_content_type" VALUES (3,'auth','group');
INSERT INTO "django_content_type" VALUES (4,'auth','user');
INSERT INTO "django_content_type" VALUES (5,'contenttypes','contenttype');
INSERT INTO "django_content_type" VALUES (6,'sessions','session');
INSERT INTO "django_content_type" VALUES (7,'personas','area');
INSERT INTO "django_content_type" VALUES (8,'personas','departamento');
INSERT INTO "django_content_type" VALUES (9,'personas','personas');
INSERT INTO "django_content_type" VALUES (10,'personas','prestamo');
INSERT INTO "auth_permission" VALUES (1,1,'add_logentry','Can add log entry');
INSERT INTO "auth_permission" VALUES (2,1,'change_logentry','Can change log entry');
INSERT INTO "auth_permission" VALUES (3,1,'delete_logentry','Can delete log entry');
INSERT INTO "auth_permission" VALUES (4,1,'view_logentry','Can view log entry');
INSERT INTO "auth_permission" VALUES (5,2,'add_permission','Can add permission');
INSERT INTO "auth_permission" VALUES (6,2,'change_permission','Can change permission');
INSERT INTO "auth_permission" VALUES (7,2,'delete_permission','Can delete permission');
INSERT INTO "auth_permission" VALUES (8,2,'view_permission','Can view permission');
INSERT INTO "auth_permission" VALUES (9,3,'add_group','Can add group');
INSERT INTO "auth_permission" VALUES (10,3,'change_group','Can change group');
INSERT INTO "auth_permission" VALUES (11,3,'delete_group','Can delete group');
INSERT INTO "auth_permission" VALUES (12,3,'view_group','Can view group');
INSERT INTO "auth_permission" VALUES (13,4,'add_user','Can add user');
INSERT INTO "auth_permission" VALUES (14,4,'change_user','Can change user');
INSERT INTO "auth_permission" VALUES (15,4,'delete_user','Can delete user');
INSERT INTO "auth_permission" VALUES (16,4,'view_user','Can view user');
INSERT INTO "auth_permission" VALUES (17,5,'add_contenttype','Can add content type');
INSERT INTO "auth_permission" VALUES (18,5,'change_contenttype','Can change content type');
INSERT INTO "auth_permission" VALUES (19,5,'delete_contenttype','Can delete content type');
INSERT INTO "auth_permission" VALUES (20,5,'view_contenttype','Can view content type');
INSERT INTO "auth_permission" VALUES (21,6,'add_session','Can add session');
INSERT INTO "auth_permission" VALUES (22,6,'change_session','Can change session');
INSERT INTO "auth_permission" VALUES (23,6,'delete_session','Can delete session');
INSERT INTO "auth_permission" VALUES (24,6,'view_session','Can view session');
INSERT INTO "auth_permission" VALUES (25,7,'add_area','Can add area');
INSERT INTO "auth_permission" VALUES (26,7,'change_area','Can change area');
INSERT INTO "auth_permission" VALUES (27,7,'delete_area','Can delete area');
INSERT INTO "auth_permission" VALUES (28,7,'view_area','Can view area');
INSERT INTO "auth_permission" VALUES (29,8,'add_departamento','Can add departamento');
INSERT INTO "auth_permission" VALUES (30,8,'change_departamento','Can change departamento');
INSERT INTO "auth_permission" VALUES (31,8,'delete_departamento','Can delete departamento');
INSERT INTO "auth_permission" VALUES (32,8,'view_departamento','Can view departamento');
INSERT INTO "auth_permission" VALUES (33,9,'add_usuario','Can add usuario');
INSERT INTO "auth_permission" VALUES (34,9,'change_usuario','Can change usuario');
INSERT INTO "auth_permission" VALUES (35,9,'delete_usuario','Can delete usuario');
INSERT INTO "auth_permission" VALUES (36,9,'view_usuario','Can view usuario');
INSERT INTO "auth_permission" VALUES (37,10,'add_prestamo','Can add prestamo');
INSERT INTO "auth_permission" VALUES (38,10,'change_prestamo','Can change prestamo');
INSERT INTO "auth_permission" VALUES (39,10,'delete_prestamo','Can delete prestamo');
INSERT INTO "auth_permission" VALUES (40,10,'view_prestamo','Can view prestamo');
INSERT INTO "auth_permission" VALUES (41,9,'add_personas','Can add personas');
INSERT INTO "auth_permission" VALUES (42,9,'change_personas','Can change personas');
INSERT INTO "auth_permission" VALUES (43,9,'delete_personas','Can delete personas');
INSERT INTO "auth_permission" VALUES (44,9,'view_personas','Can view personas');
INSERT INTO "auth_user" VALUES (1,'pbkdf2_sha256$600000$hbYXmBmMevAAcvEUd1JV18$fudRsjTh6dtezpTYtX4DMBZC9k3C0TnX/Wbm3kUXF+Q=','2023-10-11 08:12:55.567379',1,'usuario','','usuario@admin.com',1,1,'2023-10-10 00:27:33.981911','');
INSERT INTO "auth_user" VALUES (2,'pbkdf2_sha256$600000$lgNls1I2uSVkavL9Tgkr1b$0N2xTWJARKEhMVB0dkAZzqTUDmDRkYCiVkTMkZQ3yLA=','2023-10-10 07:24:08.509206',0,'jdcadenas','Cadenas','jdcadenas@gmail.com',1,1,'2023-10-10 03:58:29','José');
INSERT INTO "auth_user" VALUES (3,'pbkdf2_sha256$600000$9YcEMWb8in1R74WUsjxIcf$zR4mML/TbcseFmOxN5ocSb36A+XqsLVCWC1CuCYB/k4=','2023-10-11 08:10:19.228437',0,'usuarioprueba','Prueba','calat@mailinator.com',1,1,'2023-10-10 05:35:16','Usuario');
INSERT INTO "personas_area" VALUES (1,'Area 1');
INSERT INTO "personas_area" VALUES (2,'Area 2');
INSERT INTO "personas_area" VALUES (3,'Area 3');
INSERT INTO "personas_area" VALUES (4,'area 5');
INSERT INTO "personas_departamento" VALUES (1,'Departamento 1');
INSERT INTO "personas_departamento" VALUES (2,'departamento 2');
INSERT INTO "personas_departamento" VALUES (3,'Departamento 3');
INSERT INTO "personas_personas" VALUES (5,'Enim culpa cupidatat reiciendis hic','Ullam et eos cupiditate laborum','qyxo@mailinator.com',1,1);
INSERT INTO "personas_personas" VALUES (6,'Eum aut quia sunt nisi est lorem lorem omnis alias iste modi consequat Molestias sunt','Id exercitation beatae consequatur Quaerat ad consectetur quis praesentium est in earum nulla qui','vynuhosyt@mailinator.com',4,1);
INSERT INTO "personas_personas" VALUES (7,'aaaaaAut numquam rerum aliquam aut ea qui rerum consequatur omnis sit aliquam','Qui ex qui ad ea culpa autem adipisci','zomupofyb@mailinator.com',1,1);
INSERT INTO "django_session" VALUES ('023yu9hv0z3lm0s5e912j8aot1ea079z','.eJxVjDsOwjAQBe_iGllZfyCmpOcM1u56jQPIluKkQtwdIqWA9s3Me6mI61Li2mWOU1JnBerwuxHyQ-oG0h3rrWludZkn0puid9r1tSV5Xnb376BgL986EI2GgACzJOHgEMiBpwAcmIitdUcLA3gT8okyGvFhMImzH9lY8Or9AQVtOEk:1qq3SA:dVwVOP6Hx_MtvyAycwsg7nt2PXc5gDaiIec_pP_xgR4','2023-10-24 03:30:38.844337');
INSERT INTO "django_session" VALUES ('e5ss33hor5c4gyqvvipshhc74zc2m2j5','.eJxVjMsOwiAQRf-FtSE8hhZcuvcbyAwMUjU0Ke3K-O_apAvd3nPOfYmI21rj1nmJUxZnocXpdyNMD247yHdst1mmua3LRHJX5EG7vM6Zn5fD_Tuo2Ou3RuXAsLc6JbA2jB48lkEbxwyki3cmZNCgFVpHg09EGRBGLsoXcsGI9wfFYzdv:1qq3ze:9aVLlnNAtI_qOKz7vJOnFeYEneOw8Up8peT90oC6y0c','2023-10-24 04:05:14.144464');
INSERT INTO "django_session" VALUES ('1qrok4quud0p72vuw2xnh79u8mnxhasc','.eJxVjMsOwiAQRf-FtSE8hnZw6d5vIMMAUjUlKe3K-O_apAvd3nPOfYlA21rD1vMSpiTOQovT7xaJH3neQbrTfGuS27wuU5S7Ig_a5bWl_Lwc7t9BpV6_9RiBFZMFjdEWM2IpHlTCNCjvtAIEdtbCMIDnjEiI3pkCxGQYTc7i_QHJtTdX:1qq5U7:Iwlp3jmBIiCYMgUJ7hgIVcPyAu32N2WzRVrDy3sDjK0','2023-10-24 05:40:47.184925');
CREATE UNIQUE INDEX IF NOT EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" (
	"group_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" (
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" (
	"permission_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" (
	"user_id",
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_group_id_97559544" ON "auth_user_groups" (
	"group_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" (
	"user_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_user_id_c564eba6" ON "django_admin_log" (
	"user_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" (
	"app_label",
	"model"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" (
	"content_type_id",
	"codename"
);
CREATE INDEX IF NOT EXISTS "auth_permission_content_type_id_2f476e4b" ON "auth_permission" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "personas_usuario_area_id_e9c88eb0" ON "personas_personas" (
	"area_id"
);
CREATE INDEX IF NOT EXISTS "personas_usuario_departamento_id_05cef425" ON "personas_personas" (
	"departamento_id"
);
CREATE INDEX IF NOT EXISTS "django_session_expire_date_a5c62663" ON "django_session" (
	"expire_date"
);
CREATE INDEX IF NOT EXISTS "personas_prestamo_nombre_id_ac6c1624" ON "personas_prestamo" (
	"nombre_id"
);
COMMIT;
