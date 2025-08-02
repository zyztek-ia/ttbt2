# Arquitectura del Sistema TTBT2

Esta página describe la arquitectura de alto nivel del framework TTBT2, sus componentes principales y cómo interactúan entre sí.

## Diagrama de Arquitectura

![Diagrama de Arquitectura de TTBT2](img/ttbt1_architecture.png)
*(Nota: Este es un diagrama de ejemplo. Se debe generar y enlazar el diagrama actualizado del proyecto).*

## Componentes Principales

El framework se divide en varios directorios y módulos clave:

### 1. `core/` - El Núcleo

Este es el corazón del framework. Contiene la lógica fundamental que no está ligada a una plataforma o bot específico.

*   `bot.py`: Define la clase base `TikTokBot` que encapsula la lógica de Selenium y las interacciones principales.
*   `behavior.py`: Contiene la clase `HumanBehaviorSimulator` para realizar acciones (clics, escritura, scroll) de una manera que simula el comportamiento humano.
*   `account_manager.py`: Gestiona la carga y el acceso a las cuentas de usuario.
*   `plugin_manager.py`: Permite la carga y ejecución dinámica de plugins externos.
*   `config_loader.py`: Utilidad para cargar archivos de configuración en formato JSON y YAML.

### 2. `modules/` - Módulos de Lógica de Negocio

Este directorio contiene módulos de lógica de negocio más complejos o específicos.

*   `chatbot.py`: Implementa un chatbot simple basado en reglas.
*   `gamification_manager.py`: Gestiona la lógica y la base de datos para el sistema de gamificación.

### 3. `integrations/` - Integraciones con Servicios Externos

Aquí se encuentra el código que conecta TTBT2 con APIs y servicios de terceros.

*   `voip_gateway.py`: Contiene la lógica para interactuar con proveedores de VOIP como Twilio.
*   `telegram_bot.py`: (Ejemplo) Lógica para un bot de Telegram.

### 4. `plugins/` - Plugins Extensibles

Un directorio para alojar plugins que pueden ser cargados dinámicamente por el `PluginManager`. Los plugins permiten extender la funcionalidad del bot sin modificar el código del núcleo.

*   `api_discovery_manager.py`: Un plugin crucial que gestiona la conexión con APIs externas.

### 5. `dashboard/` - Interfaz Web

Una aplicación Flask que proporciona un dashboard y una API para monitorear y controlar el sistema.

*   `app.py`: La aplicación Flask principal y unificada.
*   `templates/`: Contiene las plantillas HTML para la interfaz de usuario.
*   **Blueprints:** La aplicación está organizada en Blueprints para cada sección (`api_config.py`, `call_center.py`, etc.).

### 6. `main.py` - Punto de Entrada

El script principal que inicia todos los componentes. Es responsable de parsear argumentos, iniciar el hilo de la aplicación web y el hilo del bot.

## Flujo de Datos y Ejecución

1.  El usuario ejecuta `main.py`.
2.  `main.py` inicia la aplicación web Flask (`dashboard/app.py`) en un hilo secundario.
3.  `main.py` inicia la sesión del `TikTokBot` en el hilo principal.
4.  El `TikTokBot` utiliza los módulos del `core` para gestionar cuentas, simular comportamiento y ejecutar su lógica.
5.  El bot puede cargar y utilizar plugins del directorio `plugins/` a través del `PluginManager`.
6.  El usuario interactúa con el `dashboard/` a través del navegador para monitorear el estado y utilizar funcionalidades como el Call Center o la configuración de APIs.
7.  El dashboard, a su vez, puede interactuar con los módulos de `integrations/` y `modules/` para realizar acciones.

Esta arquitectura modular permite un desarrollo y mantenimiento más sencillos, y facilita la adición de nuevas funcionalidades en el futuro.
