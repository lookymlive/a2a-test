# Cómo subir videos a Cloudinary desde la app Expo

1. Instala el paquete cloudinary:

   ```bash
   npm install cloudinary
   ```

2. Usa expo-image-picker para seleccionar un video.
3. Sube el video a Cloudinary usando la API y tus claves del .env.

Ejemplo básico de código (Node.js):

```js
const cloudinary = require('cloudinary').v2;
cloudinary.config({
  cloud_name: process.env.CLOUDINARY_CLOUD_NAME,
  api_key: process.env.CLOUDINARY_API_KEY,
  api_secret: process.env.CLOUDINARY_API_SECRET,
});

cloudinary.uploader.upload('ruta/al/video.mp4', { resource_type: 'video' }, (error, result) => {
  console.log(result, error);
});
```

> En Expo, deberás usar fetch para subir el archivo al endpoint de Cloudinary.
