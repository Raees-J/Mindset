# Islamic Guidance Frontend

Beautiful Next.js frontend with Aceternity UI components for the Islamic Guidance application.

## Features

- 🎨 Stunning vanishing input animation from Aceternity UI
- ⚡ Fast and responsive Next.js 14 with App Router
- 🎭 Smooth animations with Framer Motion
- 🎯 TypeScript for type safety
- 💅 Tailwind CSS for styling
- 🕌 Islamic-themed design with Arabic font support

## Getting Started

### Install Dependencies

```bash
npm install
```

### Run Development Server

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

### Build for Production

```bash
npm run build
npm start
```

## Environment Variables

Create a `.env.local` file:

```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Project Structure

```
frontend/
├── app/
│   ├── layout.tsx       # Root layout
│   ├── page.tsx         # Home page
│   └── globals.css      # Global styles
├── components/
│   ├── ui/              # UI components
│   │   └── placeholders-and-vanish-input.tsx
│   └── GuidanceCard.tsx # Result card component
├── lib/
│   ├── api.ts           # API client
│   └── utils.ts         # Utility functions
└── public/              # Static assets
```

## Features

### Vanishing Input
- Animated placeholder text rotation
- Smooth vanishing animation on submit
- Responsive design

### Guidance Cards
- Beautiful card layout for results
- Color-coded by type (Quran, Hadith, Dua)
- Arabic text with proper font
- Similarity score display

### Responsive Design
- Mobile-first approach
- Works on all screen sizes
- Touch-friendly interface

## Technologies

- **Next.js 14**: React framework with App Router
- **TypeScript**: Type-safe development
- **Tailwind CSS**: Utility-first CSS
- **Framer Motion**: Animation library
- **Axios**: HTTP client
- **Aceternity UI**: Beautiful UI components
