# Frontend del Sistema de Gestión de Candidatos (ATS) - LTI

Este directorio contiene el código del frontend para el Sistema de Seguimiento de Candidatos (ATS) de LTI, desarrollado con Angular.

## Requisitos previos

- Node.js 18 o superior
- npm 9 o superior
- Angular CLI 16 o superior

## Instalación

1. Instalar las dependencias:

```bash
npm install
```

2. Configurar las variables de entorno (si es necesario)

## Ejecución

Para iniciar el servidor de desarrollo:

```bash
ng serve
```

La aplicación estará disponible en http://localhost:4200

## Construcción

Para construir la aplicación para producción:

```bash
ng build --prod
```

Los archivos generados se encontrarán en el directorio `dist/`.

## Pruebas

Para ejecutar las pruebas unitarias:

```bash
ng test
```

Para ejecutar las pruebas end-to-end:

```bash
ng e2e
```

## Estructura del proyecto

```
frontend/
├── src/                  # Código fuente
│   ├── app/              # Componentes, servicios, etc.
│   │   ├── components/   # Componentes reutilizables
│   │   ├── models/       # Modelos de datos
│   │   ├── services/     # Servicios para comunicación con la API
│   │   └── pages/        # Páginas de la aplicación
│   ├── assets/           # Recursos estáticos
│   └── environments/     # Configuración de entornos
├── angular.json          # Configuración de Angular
├── package.json          # Dependencias del proyecto
└── tsconfig.json         # Configuración de TypeScript
``` 