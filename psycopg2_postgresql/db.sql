create database if not exists Evaluacion_Empleados;
use Evaluacion_Empleados;

create table if not exists Empleado (
    id_empleado int AUTO_INCREMENT,
    nombre varchar(30),
    apellido varchar(30),
    puesto varchar(25),
    supervisor varchar(50),
    fecha_contratacion date,

    constraint pk_empleado primary key (id_empleado)
);

create table if not exists Archivo_Empleado (
    id_archivo_e int,
    id_empleado_a int,
    ruta varchar(250),
    nombre_real varchar(50),

    constraint fk_archivo foreign key (id_archivo_e) references ARCHIVO (id_archivo),
    constraint fk_usuario foreign key (id_empleado_a) references EMPLEADO (id_empleado),
    constraint pk_archivo_empleado primary key (id_archivo_u, id_usuario_a, nombre_real)
);

CREATE TABLE IF NOT EXISTS Archivo (
    id_archivo int AUTO_INCREMENT,
    nombre_archivo varchar(35),

    constraint pk_archivo primary key (id_archivo)
);