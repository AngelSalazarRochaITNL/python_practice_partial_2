create database if not exists Evaluacion_Empleados;
use Evaluacion_Empleados;

create table if not exists Evaluacion (
    id_evaluacion int AUTO_INCREMENT,
    fecha_evaluacion date,
    desempenio char(1),
    emp_clave varchar(10),
    evaluado_por varchar(250),

    constraint pk_evaluacion primary key (id_evaluacion),
    constraint fk_empleado foreign key (emp_clave) REFERENCES Empleado (id_empleado) ON DELETE NO ACTION ON UPDATE NO ACTION
);

create table if not exists Respuesta (
    id int AUTO_INCREMENT,
    numero char(1) not null,
    inciso char(1) not null,
    id_evaluacion int,
    puntuacion char(1),
    comentario varchar(250),

    CONSTRAINT chk_puntuacion CHECK (puntuacion >= 0 and puntuacion <= 3),
    CONSTRAINT pk_respuesta primary key (id,numero,inciso),
    CONSTRAINT fk_numero foreign key (numero) references Punto (num_punto),
    CONSTRAINT fk_inciso foreign key (inciso) references Punto (inciso),
    constraint fk_evaluacion foreign key (id_evaluacion) references evaluacion (id_evaluacion)
);

create table if not exists Punto (
    num_punto int not null,
    inciso char(1) not null,
    pregunta varchar(80),

    CONSTRAINT pk_punto primary key (num_punto,inciso)
);

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
    constraint pk_archivo_empleado primary key (id_archivo_u, id_empleado_a, nombre_real)
);

CREATE TABLE IF NOT EXISTS Archivo (
    id_archivo int AUTO_INCREMENT,
    nombre_archivo varchar(35),

    constraint pk_archivo primary key (id_archivo)
);

INSERT INTO archivo ('nombre_archivo')
VALUES 	('Comprobante de Estudios'),
		('Acta de Nacimiento'),
        ('Identificacion Oficial'),
        ('Seguro Social'),
        ('Comprobante de Domicilio'),
        ('Carta de No Antecedentes Penales'),
        ('Examen Antidopaje'),
        ('Referencias'),
        ('Capacitacion'),
        ('Control empleado'),
        ('Otros');

INSERT INTO punto ('num_punto, inciso, pregunta')
VALUES (1,'a','a Precisión y calidad del trabajo realizado'),
	(1,'b','b Cantidad de trabajo completado'),
    (1,'c','c Organización del trabajo en tiempo y forma'),
    (1,'d','d Cuidado de herramientas y equipo'),
    
    (2,'a','a Nivel de experiencia y conocimiento técnico para el trabajo requerido'),
	(2,'b','b Uso y conocimiento de métodos y procedimientos'),
    (2,'c','c Uso y conocimiento de herramientas'),
    (2,'d','d Puede desempeñarse con poca o ninguna ayuda'),
    (2,'e','e Capacidad de enseñar / entrenar a otros'),

    (3,'a','a Trabaja sin necesidad de supervisión'),
	(3,'b','b Se esfuerza más si la situación lo requiere'),
    (3,'c','c Puntualidad'),
    (3,'d','d Asistencia'),
    (3,'e','e Uniforme'),

    (4,'a','a Cuando completa sus tareas, busca nuevas asignaciones'),
	(4,'b','b Elige prioridades de forma eficiente'),
    (4,'c','c Sugiere mejoras'),
    (4,'d','d Identifica errores y trabaja para arreglarlos'),
    (4,'e','e Motiva y ayuda a los demás'),

    (5,'a','a Trabaja fluidamente con supervisores, pares y subordinados'),
	(5,'b','b Tiene una actitud positiva y proactiva'),
    (5,'c','c Promueve el trabajo en equipo');