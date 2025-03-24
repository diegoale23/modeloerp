# Manual de Usuario - ModeloERP

## Introducción

**ModeloERP** es un sistema de gestión empresarial que permite administrar usuarios, inventario, finanzas, proveedores, pedidos y reportes. Este manual proporciona instrucciones detalladas para utilizar cada módulo del sistema.

---

## Índice

- [Inicio de Sesión](#inicio-de-sesión)
- [Gestión de Usuarios-Clientes](#gestión-de-usuarios-clientes)
- [Gestión de Inventario](#gestión-de-inventario)
- [Gestión Financiera](#gestión-financiera)
- [Gestión de Proveedores](#gestión-de-proveedores)
- [Gestión de Pedidos](#gestión-de-pedidos)
- [Generación de Reportes](#generación-de-reportes)
- [Cierre de Sesión](#cierre-de-sesión)
- [Notas Adicionales](#notas-adicionales)

---

## Inicio de Sesión

1. Accede al sistema desde la URL principal del proyecto.

http://127.0.0.1:5000/
  
3. Ingresa tus credenciales:

   - **Usuario**: dacp23.
   - **Contraseña**: manzana232.

5. Haz clic en el botón **Iniciar Sesión**.

![image](https://github.com/user-attachments/assets/c55f509b-55c7-446c-a929-783c2d0551c1)

6. Si las credenciales son correctas, serás redirigido al panel principal.

![image](https://github.com/user-attachments/assets/3f993edd-18ce-403b-ac4f-29bc04c72346)

---

## Gestión de Usuarios - Clientes

![image](https://github.com/user-attachments/assets/81e44a3f-cc9b-4022-9465-10ff4712faf7)

### Crear un Usuario
1. Ve al módulo **Usuarios** desde el menú principal.
2. Haz clic en **Agregar Usuario**.
3. Completa los campos requeridos:
   - Nombre
   - Apellido
   - Correo electrónico

4. Haz clic en **Guardar** para registrar el usuario.

![image](https://github.com/user-attachments/assets/de5afdcf-792f-41c8-ac1d-89e39af3cb0d)

### Editar un Usuario
1. En la lista de usuarios, selecciona el usuario que deseas editar.
2. Realiza los cambios necesarios.
3. Haz clic en **Guardar**.

![image](https://github.com/user-attachments/assets/83e36070-e266-4513-ac8d-2675b0408191)

### Eliminar un Usuario
1. En la lista de usuarios, selecciona el usuario que deseas eliminar.
2. Haz clic en **Eliminar** y confirma la acción.

![image](https://github.com/user-attachments/assets/36ce1622-1723-4f66-bcbf-93a455015680)

---

## Gestión de Inventario

![image](https://github.com/user-attachments/assets/5e2111dc-9ee5-4e12-8cce-60eeccfbb195)

### Agregar un Producto
1. Ve al módulo **Inventario**.
2. Haz clic en **Agregar Producto**.
3. Completa los campos requeridos:
   - Nombre
   - Descripción
   - Precio
   - Stock inicial
4. Haz clic en **Guardar**.

![image](https://github.com/user-attachments/assets/ee3772d4-136c-4695-80a9-d7c58916719f)

### Registrar un Movimiento de Inventario
1. Selecciona un producto de la lista.
2. Haz clic en **Registrar Movimiento**.
3. Selecciona el tipo de movimiento:
   - Entrada (aumenta el stock)
   - Salida (reduce el stock)
4. Ingresa la cantidad y una descripción opcional.
5. Haz clic en **Guardar**.

![image](https://github.com/user-attachments/assets/407a853f-aa30-4aa4-821e-e9d4a0ff7afc)

---

## Gestión Financiera

![image](https://github.com/user-attachments/assets/5fe3180f-1674-4c99-94f1-33ac2503be97)

### Registrar un Ingreso o Gasto
1. Ve al módulo **Gestión Financiera**.
2. Haz clic en **Registrar Movimiento**.
3. Selecciona el tipo de movimiento:
   - Ingreso
   - Gasto
4. Completa los campos requeridos:
   - Monto
   - Descripción
   - Fecha
5. Haz clic en **Guardar**.

![image](https://github.com/user-attachments/assets/6a12fb63-4212-4cf7-99b5-2a20e05d7c8a)

### Consultar el Balance Financiero
1. Ve al módulo **Gestión Financiera**.
2. Selecciona el rango de fechas deseado.
3. Visualiza el balance total, ingresos y gastos.

![image](https://github.com/user-attachments/assets/acc02a38-952e-45d4-baf1-01003244b010)

---

## Gestión de Proveedores

![image](https://github.com/user-attachments/assets/4246974a-c157-4254-be4f-003f66a447a9)

### Agregar un Proveedor
1. Ve al módulo **Proveedores**.
2. Haz clic en **Agregar Proveedor**.
3. Completa los campos requeridos:
   - Nombre
   - Contacto
   - Dirección
   - Teléfono
   - Correo electrónico
4. Haz clic en **Guardar**.

![image](https://github.com/user-attachments/assets/27f263a1-97d5-4edc-9634-8b4863ce4db6)

### Asociar Productos a un Proveedor
1. Selecciona un proveedor de la lista.
2. Haz clic en **Asociar Productos**.
3. Selecciona los productos que deseas asociar.
4. Haz clic en **Guardar**.

![image](https://github.com/user-attachments/assets/807ee7d8-b56e-4d83-ab3c-f71c6d0a5281)

---

## Gestión de Pedidos

![image](https://github.com/user-attachments/assets/59fafe37-2289-4b78-9ecb-834abd1ab5a6)

### Crear un Pedido
1. Ve al módulo **Pedidos**.
2. Haz clic en **Crear Pedido**.
3. Selecciona el cliente.
4. Agrega los productos al pedido, especificando la cantidad.
5. Haz clic en **Guardar**.

![image](https://github.com/user-attachments/assets/b99b6927-009a-401c-ad99-f6524f529481)

### Consultar Pedidos
1. Ve al módulo **Pedidos**.
2. Filtra los pedidos por cliente o fecha.
3. Haz clic en un pedido para ver los detalles.

![image](https://github.com/user-attachments/assets/00f4fe9f-d08e-4796-a55e-2b1257cbe934)

---

## Generación de Reportes

![image](https://github.com/user-attachments/assets/b0162fea-e8ff-4db2-a49e-75150a7cd6d6)

### Generar un Reporte
1. Ve al módulo **Reportes**.
2. Selecciona el tipo de reporte:
   - Financiero
   - Inventario
   - Pedidos
   - Proveedores
3. Ingresa los parámetros requeridos (por ejemplo, rango de fechas).
4. Haz clic en **Generar Reporte**.
5. Descarga o visualiza el reporte generado.

![image](https://github.com/user-attachments/assets/0c0a52a9-6d0f-4ac7-9d94-05f9a70214fc)

---

## Cierre de Sesión

1. Haz clic en tu nombre de usuario en la esquina superior derecha.
2. Selecciona **Cerrar Sesión**.
3. Serás redirigido a la página de inicio de sesión.

![image](https://github.com/user-attachments/assets/8b6740d4-e37c-434e-a209-3decb2fd8940)

---

## Notas Adicionales

- **La creación de usuarios para acceso al sistema esta delegada exclusivamente al superusuario**:
  - **Administrador**: Acceso completo a todas las funcionalidades.
  - **GrupoFinanciera**: Acceso a los formularios de gestión financiera y reportes, limitadas las funcionalidades de acuerdo al jefe de la oficina Financiera.
  - **Inventarios y Almacenistas**: Acceso a los formularios de Inventarios, proveedores, clientes, pedidos y reportes; limitadas las funcionalidades de acuerdo al jefe de la oficina Financiera.

- **Recomendaciones**:
  - Mantén tus credenciales seguras.
  - Realiza copias de seguridad periódicas de la base de datos.

---

Este manual cubre las funcionalidades principales del sistema. Si necesitas más información o soporte, contacta al administrador del sistema.
