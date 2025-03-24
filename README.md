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
  - [Pedidos](#pedidos)
  - [Reportes](#reportes)
- [Diagramas](#diagramas)
  - [Diagramas de Clases](#diagrama-de-clases)
  - [Diagrama Entidad-Relación](#diagrama-entidad-relación)
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
- **Pedidos**: Gestión de pedidos realizados por los clientes.
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

### Pedidos
El modelo Pedido permite gestionar los pedidos realizados por los clientes. Incluye información como el cliente, los productos solicitados, la cantidad y el total del pedido.

### Reportes

El modelo `Reporte` permite generar reportes financieros, de inventario, pedidos y proveedores. Los reportes se generan dinámicamente según los parámetros proporcionados.

---

## Diagramas

### Diagrama de Clases

![Diagrama de Clases](out/diagrama_clases/diagrama_clases.png)

### Diagrama Entidad-Relación

![Diagrama Entidad-Relación](out/entidad_relacion_erp/entidad_relacion_erp.png)

### Usuarios

- Casos de Uso
  
![Diagramas de Caso de Uso](out/ERP/usuarios/use_case_diagram/use_case_diagram.png)

- Diagramas de Objetos
  
![Diagramas de Objetos](out/ERP/usuarios/diagrama_objetos_usuarios/diagrama_objetos_usuarios.png)

- Diagramas de Secuencia

![Diagramas de Secuencia](out/ERP/usuarios/sequence_diagram/sequence_diagram.png)
  
- Diagramas de Colaboración

![Diagramas de Colaboración](out/ERP/usuarios/collaboration_diagram/collaboration_diagram.png)

- Diagramas de Estados

![Diagramas de Estados](out/ERP/usuarios/state_diagram/state_diagram.png)

- Diagramas de Componentes

![Diagramas de Componentes](out/ERP/usuarios/component_diagram/component_diagram.png)

- Diagramas de Despliegue

![Diagramas de Despliegue](out/ERP/usuarios/deployment_diagram/deployment_diagram.png)

### Inventario

- Casos de Uso
  
![Diagramas de Caso de Uso](out/ERP/inventario/use_case_diagram/use_case_diagram.png)

- Diagramas de Objetos
  
![Diagramas de Objetos](out/ERP/inventario/diagrama_objetos_inventario/diagrama_objetos_inventario.png)

- Diagramas de Secuencia

![Diagramas de Secuencia](out/ERP/inventario/sequence_diagram/sequence_diagram.png)
  
- Diagramas de Colaboración

![Diagramas de Colaboración](out/ERP/inventario/collaboration_diagram/collaboration_diagram.png)

- Diagramas de Estados

![Diagramas de Estados](out/ERP/inventario/state_diagram/state_diagram.png)

- Diagramas de Componentes

![Diagramas de Componentes](out/ERP/inventariocomponent_diagram/component_diagram.png)

- Diagramas de Despliegue

![Diagramas de Despliegue](out/ERP/inventario/deployment_diagram/deployment_diagram.png)
  
### Gestión Financiera

- Casos de Uso
  
![Diagramas de Caso de Uso](out/ERP/gestion_financiera/use_case_diagram/use_case_diagram.png)

- Diagramas de Objetos
  
![Diagramas de Objetos](out/ERP/gestion_financiera/diagrama_objetos_gestion_financiera/diagrama_objetos_gestion_financiera.png)

- Diagramas de Secuencia

![Diagramas de Secuencia](out/ERP/gestion_financiera/sequence_diagram/sequence_diagram.png)
  
- Diagramas de Colaboración

![Diagramas de Colaboración](out/ERP/gestion_financiera/collaboration_diagram/collaboration_diagram.png)

- Diagramas de Estados

![Diagramas de Estados](out/ERP/gestion_financiera/state_diagram/state_diagram.png)

- Diagramas de Componentes

![Diagramas de Componentes](out/ERP/gestion_financiera/component_diagram/component_diagram.png)

- Diagramas de Despliegue

![Diagramas de Despliegue](out/ERP/gestion_financiera/deployment_diagram/deployment_diagram.png)
  
### Proveedores

- Casos de Uso
  
![Diagramas de Caso de Uso](out/ERP/proveedores/use_case_diagram/use_case_diagram.png)

- Diagramas de Objetos
  
![Diagramas de Objetos](out/ERP/proveedores/diagrama_objetos_proveedores/diagrama_objetos_proveedores.png)

- Diagramas de Secuencia

![Diagramas de Secuencia](out/ERP/proveedores/sequence_diagram/sequence_diagram.png)
  
- Diagramas de Colaboración

![Diagramas de Colaboración](out/ERP/proveedores/collaboration_diagram/collaboration_diagram.png)

- Diagramas de Estados

![Diagramas de Estados](out/ERP/proveedores/state_diagram/state_diagram.png)

- Diagramas de Componentes

![Diagramas de Componentes](out/ERP/proveedores/component_diagram/component_diagram.png)

- Diagramas de Despliegue

![Diagramas de Despliegue](out/ERP/proveedores/deployment_diagram/deployment_diagram.png)
  
### Pedidos

- Casos de Uso
  
![Diagramas de Caso de Uso](out/ERP/pedidos/use_case_diagram/use_case_diagram.png)

- Diagramas de Objetos
  
![Diagramas de Objetos](out/ERP/pedidos/diagrama_objetos_pedidos/diagrama_objetos_pedidos.png)

- Diagramas de Secuencia

![Diagramas de Secuencia](out/ERP/pedidos/sequence_diagram/sequence_diagram.png)
  
- Diagramas de Colaboración

![Diagramas de Colaboración](out/ERP/pedidos/collaboration_diagram/collaboration_diagram.png)

- Diagramas de Estados

![Diagramas de Estados](out/ERP/pedidos/state_diagram/state_diagram.png)

- Diagramas de Componentes

![Diagramas de Componentes](out/ERP/pedidos/component_diagram/component_diagram.png)

- Diagramas de Despliegue

![Diagramas de Despliegue](out/ERP/pedidos/deployment_diagram/deployment_diagram.png)

### Reportes

- Casos de Uso
  
![Diagramas de Caso de Uso](out/ERP/reportes/use_case_diagram/use_case_diagram.png)

- Diagramas de Secuencia
  
![Diagramas de Secuencia](out/ERP/reportes/sequence_diagram/sequence_diagram.png)
  
- Diagramas de Colaboración

![Diagramas de Colaboración](out/ERP/reportes/collaboration_diagram/collaboration_diagram.png)

- Diagramas de Estados

![Diagramas de Estados](out/ERP/reportes/state_diagram/state_diagram.png)

- Diagramas de Componentes

![Diagramas de Componentes](out/ERP/reportes/component_diagram/component_diagram.png)

- Diagramas de Despliegue

![Diagramas de Despliegue](out/ERP/reportes/deployment_diagram/deployment_diagram.png)

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
