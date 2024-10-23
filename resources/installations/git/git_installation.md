
# Instalación de Git en macOS, Windows y Linux

## 1. Instalación de Git en macOS

### Método 1: Usando Homebrew (Recomendado)
1. Abre la **Terminal**.
2. Verifica si tienes instalado Homebrew ejecutando `brew --version`, si el luego puedes ver la version de Homebrew, lo tienes instalado correctamente.
3. Si no tienes instalado Homebrew, instálalo con este comando:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
4. Instala Git con el siguiente comando:
   ```bash
   brew install git
   ```
5. Verifica la instalación de Git:
   ```bash
   git --version
   ```
   Deberías ver la versión de Git instalada.

### Método 2: Descarga Directa
1. Visita el sitio web oficial de Git: [https://git-scm.com](https://git-scm.com).
2. Descarga el instalador para macOS.
3. Abre el archivo `.dmg` y sigue las instrucciones en pantalla para completar la instalación.
4. Abre la **Terminal** y verifica la instalación ejecutando:
   ```bash
   git --version
   ```

## 2. Instalación de Git en Windows

### Método 1: Usando Git Bash
1. Ve al sitio oficial de Git: [https://git-scm.com](https://git-scm.com).
2. Haz clic en **Download for Windows** para descargar el instalador `.exe`.
3. Abre el archivo `.exe` y sigue las instrucciones del asistente de instalación:
   - Acepta los términos y condiciones.
   - Selecciona las opciones por defecto o personaliza la instalación según tus necesidades.
4. Una vez completada la instalación, abre **Git Bash** (que se habrá instalado automáticamente).
5. Verifica la instalación ejecutando:
   ```bash
   git --version
   ```
   Deberías ver la versión de Git instalada.

## 3. Instalación de Git en Linux

### Método 1: Usando el Gestor de Paquetes (Debian/Ubuntu)
1. Abre la **Terminal**.
2. Actualiza la lista de paquetes:
   ```bash
   sudo apt update
   ```
3. Instala Git con el siguiente comando:
   ```bash
   sudo apt install git
   ```
4. Verifica la instalación de Git:
   ```bash
   git --version
   ```

### Método 2: Usando el Gestor de Paquetes (Fedora)
1. Abre la **Terminal**.
2. Instala Git con el siguiente comando:
   ```bash
   sudo dnf install git
   ```
3. Verifica la instalación de Git:
   ```bash
   git --version
   ```

### Método 3: Compilar desde el Código Fuente
Si prefieres la versión más reciente de Git o no está disponible en el repositorio de tu distribución, puedes compilarla manualmente:
1. Instala las dependencias necesarias:
   ```bash
   sudo apt update
   sudo apt install make libssl-dev libghc-zlib-dev libcurl4-gnutls-dev libexpat1-dev gettext unzip
   ```
2. Descarga el código fuente desde [https://git-scm.com](https://git-scm.com).
3. Extrae y compila Git:
   ```bash
   tar -zxf git-*.tar.gz
   cd git-*
   make prefix=/usr/local all
   sudo make prefix=/usr/local install
   ```
4. Verifica la instalación:
   ```bash
   git --version
   ```

## Configuración Inicial de Git

Una vez instalado Git, es importante configurarlo globalmente:
1. Configura tu nombre de usuario:
   ```bash
   git config --global user.name "Tu Nombre"
   ```
2. Configura tu correo electrónico:
   ```bash
   git config --global user.email "tu.email@example.com"
   ```

Con esto, Git estará listo para usarse en tu sistema.
