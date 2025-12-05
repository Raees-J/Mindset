# Convert to Progressive Web App (PWA)

## What is a PWA?
A Progressive Web App allows users to "install" your website on their phone/desktop like a native app, with:
- Home screen icon
- Offline functionality
- Push notifications
- Native app-like experience

## Setup Steps

### 1. Install Dependencies
```bash
npm install next-pwa
```

### 2. Update next.config.js
```javascript
const withPWA = require('next-pwa')({
  dest: 'public',
  register: true,
  skipWaiting: true,
  disable: process.env.NODE_ENV === 'development'
});

module.exports = withPWA({
  reactStrictMode: true,
});
```

### 3. Create manifest.json
```json
{
  "name": "Islamic Guidance",
  "short_name": "Islamic Guidance",
  "description": "Find peace through Quran and Sunnah",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#f5f5dc",
  "theme_color": "#1a5f3f",
  "orientation": "portrait",
  "icons": [
    {
      "src": "/icon-192x192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/icon-512x512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ]
}
```

### 4. Update layout.tsx
```typescript
export const metadata = {
  manifest: '/manifest.json',
  themeColor: '#1a5f3f',
  appleWebApp: {
    capable: true,
    statusBarStyle: 'default',
    title: 'Islamic Guidance'
  }
};
```

### 5. Add Icons
Place these in `public/` folder:
- icon-192x192.png
- icon-512x512.png
- apple-touch-icon.png

### Benefits
✅ Works on iOS and Android
✅ No app store approval needed
✅ Instant updates
✅ Smaller size than native apps
✅ One codebase for all platforms

### Installation
Users can install by:
1. Visit website in browser
2. Click "Add to Home Screen" (iOS) or "Install" (Android)
3. App appears on home screen like native app
