# Guía de Instalación de TTBT2

Sigue estos pasos para tener una instancia funcional de TTBT2 en tu entorno local usando Docker, el método recomendado para un despliegue rápido y consistente.

## Prerrequisitos

1.  **Git:** Para clonar el repositorio. [Instalar Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
2.  **Docker y Docker Compose:** Para construir y ejecutar la aplicación en contenedores. [Instalar Docker](https://docs.docker.com/get-docker/).

## Paso 1: Clonar el Repositorio

Abre tu terminal y clona el repositorio oficial de TTBT2 desde GitHub:

```bash
git clone https://github.com/zyztek/ttbt2.git
cd ttbt2
```

## Paso 2: Configuración Inicial

El proyecto requiere algunos archivos de configuración básicos para funcionar. Aunque puedes personalizarlos más tarde, puedes empezar con los ejemplos.

*   **Cuentas:** Edita `accounts.json` para añadir las cuentas que usarán tus bots.
*   **Proxies:** Edita `proxies/proxies.json` para añadir tus proxies.
*   **Fingerprints:** Edita `fingerprints/fingerprints.json` para añadir fingerprints de navegador.

*Nota: El repositorio incluye archivos de ejemplo que puedes renombrar y modificar.*

## Paso 3: Construir y Ejecutar con Docker Compose

El método más sencillo para levantar toda la aplicación (Bot, Dashboard, y servicios de monitoreo) es usando el `docker-compose.yaml` que se encuentra en la carpeta `monitoring/`.

Desde la raíz del proyecto, ejecuta el siguiente comando:

```bash
docker-compose -f monitoring/docker-compose.yaml up --build -d
```

*   `--build`: Fuerza la reconstrucción de la imagen de Docker si has hecho cambios en el código.
*   `-d`: Ejecuta los contenedores en modo "detached" (en segundo plano).

## Paso 4: Verificar la Instalación

Una vez que los contenedores estén en ejecución, puedes verificar que todo funciona correctamente:

1.  **Dashboard Web:** Abre tu navegador y ve a `http://localhost:5000`. Deberías ver el panel de control principal de TTBT2.
2.  **Logs del Bot:** Puedes ver la salida del contenedor del bot para verificar que se ha iniciado sin errores:
    ```bash
    docker logs -f ttbt2-bot # (El nombre puede variar, usa 'docker ps' para verlo)
    ```
3.  **Servicios de Monitoreo:**
    *   **Prometheus:** `http://localhost:9090`
    *   **Grafana:** `http://localhost:3000`

## Solución de Problemas

*   **Error de Puerto Ocupado:** Si el puerto 5000 (o 9090/3000) ya está en uso en tu máquina, puedes cambiarlo en el archivo `docker-compose.yaml` antes de ejecutar el comando `up`.
*   **Errores de Build de Docker:** Asegúrate de tener la última versión de Docker y Docker Compose. Si los problemas persisten, intenta un `docker system prune -a` para limpiar builds antiguos y vuelve a intentarlo.

¡Felicidades! Ahora tienes una instancia completa de TTBT2 funcionando localmente. Explora el dashboard, prueba las funcionalidades y prepárate para extender el framework.
