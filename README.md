# ModeloERP

ModeloERP es un sistema de gestión empresarial desarrollado en Django. Este proyecto incluye módulos para la gestión de usuarios, inventario, finanzas, proveedores y reportes, proporcionando una solución integral para la administración de una empresa.

## Tabla de Contenidos

- [Descripción General](#descripción-general)
- [Características](#características)
- [Instalación](#instalación)
- [Modelos](#modelos)
  - [Usuarios](#usuarios)
  - [Inventario](#inventario)
  - [Gestión Financiera](#gestión-financiera)
  - [Proveedores](#proveedores)
  - [Reportes](#reportes)
- [Diagramas UML](#diagramas-uml)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

---

## Descripción General

ModeloERP es un sistema modular que permite gestionar diferentes aspectos de una empresa, como usuarios, inventario, finanzas, proveedores y reportes. Está diseñado para ser flexible y escalable, permitiendo su personalización según las necesidades del negocio.

---

## Características

- **Gestión de Usuarios**: Control de usuarios con roles personalizados (`administrador`, `empleado`, `cliente`).
- **Inventario**: Gestión de productos y movimientos de inventario (entradas y salidas).
- **Gestión Financiera**: Registro de ingresos y gastos, generación de informes financieros.
- **Proveedores**: Administración de proveedores y sus productos asociados.
- **Reportes**: Generación de reportes dinámicos para finanzas, inventario, pedidos y proveedores.

---

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/diegoale23/modeloerp.git
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Realiza las migraciones:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Inicia el servidor:
   ```bash
   python manage.py runserver
   ```

---

## Modelos

### Usuarios

El modelo `Usuario` extiende el modelo `AbstractUser` de Django y permite gestionar usuarios con roles personalizados como `administrador`, `empleado` y `cliente`.

### Inventario

- **Producto**: Representa los productos en el inventario, con atributos como nombre, descripción, precio y stock.
- **MovimientoInventario**: Registra entradas y salidas de productos en el inventario.

### Gestión Financiera

- **RegistroFinanciero**: Registra ingresos y gastos asociados a usuarios.
- **InformeFinanciero**: Genera informes financieros basados en un rango de fechas.

### Proveedores

El modelo `Proveedor` permite gestionar proveedores y sus productos asociados mediante una relación de muchos a muchos.

### Reportes

El modelo `Reporte` permite generar reportes financieros, de inventario, pedidos y proveedores. Los reportes se generan dinámicamente según los parámetros proporcionados.

---

## Diagramas UML

### Usuarios

![Diagrama de Usuarios](out/usuarios/diagrama_usuarios.png)

### Inventario

![Diagrama de Inventario](out/inventario/diagrama_inventario.png)

### Gestión Financiera

![Diagrama de Gestión Financiera](out/gestion_financiera/diagrama_gestion_financiera.png)

### Proveedores

![Diagrama de Proveedores](out/proveedores/diagrama_proveedores.png)

### Reportes

![Diagrama de Reportes](out/reportes/diagrama_reportes.png)

---

## Contribuciones

¡Las contribuciones son bienvenidas! Por favor, abre un issue o envía un pull request para sugerir mejoras o reportar errores.

---

## Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).
```

### Notas:
1. **Ubicación de los diagramas**: Asegúrate de que los diagramas estén en las rutas especificadas:
   - `out/usuarios/diagrama_usuarios.png`
   - `out/inventario/diagrama_inventario.png`
   - `out/gestion_financiera/diagrama_gestion_financiera.png`
   - `out/proveedores/diagrama_proveedores.png`
   - `out/reportes/diagrama_reportes.png`

2. **Formato de los diagramas**: Si los diagramas no están en formato `.png`, ajusta las extensiones en los enlaces (por ejemplo, `.svg` o `.jpg`).

3. **Repositorio**: Reemplaza `https://github.com/tu_usuario/modeloerp.git` con la URL de tu repositorio.

¿Te gustaría agregar algo más o necesitas ayuda con los diagramas?
