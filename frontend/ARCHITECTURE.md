# Frontend Architecture

## Overview

The frontend follows **React best practices** with Next.js 14 App Router, TypeScript, and component-based architecture.

## Directory Structure

```
frontend/
├── app/                    # Next.js App Router
│   ├── layout.tsx         # Root layout
│   ├── page.tsx           # Home page
│   └── globals.css        # Global styles
│
├── components/            # React components
│   ├── ui/               # Reusable UI components
│   │   └── placeholders-and-vanish-input.tsx
│   ├── ErrorBoundary.tsx # Error boundary component
│   ├── ErrorMessage.tsx  # Error display component
│   ├── Footer.tsx        # Footer component
│   ├── GuidanceCard.tsx  # Result card component
│   ├── Header.tsx        # Header component
│   ├── LoadingState.tsx  # Loading indicator
│   ├── ResultsSection.tsx # Results display
│   └── SearchSection.tsx # Search input section
│
├── hooks/                 # Custom React hooks
│   └── useGuidance.ts    # Guidance fetching hook
│
├── lib/                   # Utilities and helpers
│   ├── api.ts            # API client with error handling
│   ├── constants.ts      # App constants
│   └── utils.ts          # Utility functions
│
└── public/               # Static assets
```

## Design Patterns

### 1. Component Composition
Components are small, focused, and composable:
- **Header**: Site branding and title
- **SearchSection**: Search input with placeholders
- **ResultsSection**: Grid of result cards
- **GuidanceCard**: Individual result display
- **Footer**: Site footer

### 2. Custom Hooks
Business logic extracted into reusable hooks:
```typescript
const { results, loading, error, fetchGuidance, reset } = useGuidance();
```

### 3. Error Boundary
React Error Boundary catches and handles component errors gracefully.

### 4. Separation of Concerns
- **Components**: UI rendering
- **Hooks**: State management and side effects
- **API Layer**: HTTP requests and error handling
- **Constants**: Configuration values

### 5. TypeScript
Full type safety throughout the application:
- Interface definitions for all data structures
- Type-safe API client
- Proper typing for props and state

## Best Practices Implemented

### Code Quality
1. **TypeScript**: Full type safety
2. **ESLint**: Code linting
3. **Prettier**: Code formatting (via Next.js)
4. **Memoization**: `memo()` for expensive components
5. **Semantic HTML**: Proper HTML5 elements

### Performance
1. **Code Splitting**: Automatic with Next.js
2. **Image Optimization**: Next.js Image component ready
3. **Lazy Loading**: Components load on demand
4. **Memoization**: Prevent unnecessary re-renders
5. **Efficient Re-renders**: Proper dependency arrays

### Accessibility
1. **ARIA Labels**: Proper labeling for screen readers
2. **Semantic HTML**: `<article>`, `<header>`, `<footer>`, etc.
3. **Keyboard Navigation**: Full keyboard support
4. **Focus Management**: Proper focus indicators
5. **Language Attributes**: `lang="ar"` for Arabic text

### Error Handling
1. **Error Boundary**: Catches React errors
2. **API Error Handling**: Proper error messages
3. **Loading States**: Clear feedback to users
4. **Retry Logic**: Can be added to API client
5. **Graceful Degradation**: Fallback UI

### State Management
1. **Custom Hooks**: Encapsulated state logic
2. **Local State**: Component-level state
3. **No Global State**: Not needed for this app
4. **Proper Cleanup**: useCallback for stable references

## Component Architecture

### Smart vs Presentational Components

**Smart Components** (Container):
- `app/page.tsx`: Main page with business logic
- `SearchSection.tsx`: Handles search state

**Presentational Components**:
- `GuidanceCard.tsx`: Pure display component
- `Header.tsx`: Static header
- `Footer.tsx`: Static footer
- `LoadingState.tsx`: Loading indicator

## API Layer

### Features
1. **Axios Instance**: Configured HTTP client
2. **Interceptors**: Request/response handling
3. **Error Handling**: Custom ApiError class
4. **Type Safety**: Full TypeScript support
5. **Timeout Handling**: 30-second timeout
6. **Base URL Configuration**: Environment-based

### Error Handling Flow
```
API Call → Axios Interceptor → Custom ApiError → Hook → Component → UI
```

## Styling

### Tailwind CSS
- **Utility-First**: Rapid development
- **Custom Theme**: Islamic colors defined
- **Responsive**: Mobile-first approach
- **Dark Mode Ready**: Can be enabled

### Custom Styles
- **Arabic Font**: Amiri font for Arabic text
- **Animations**: Framer Motion for smooth transitions
- **Gradients**: Islamic-themed color scheme

## Animation Strategy

### Framer Motion
1. **Page Transitions**: Smooth entry/exit
2. **Staggered Children**: Cards animate in sequence
3. **Hover Effects**: Interactive feedback
4. **Loading States**: Animated spinners

### Performance
- **GPU Acceleration**: Transform and opacity
- **Will-Change**: Optimized animations
- **Reduced Motion**: Respects user preferences

## Data Flow

```
User Input
    ↓
SearchSection (onChange)
    ↓
useGuidance Hook (fetchGuidance)
    ↓
API Client (getGuidance)
    ↓
Backend API
    ↓
Response/Error
    ↓
Hook State Update
    ↓
Component Re-render
    ↓
ResultsSection/ErrorMessage
```

## Environment Variables

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Testing Strategy (Future)

### Unit Tests
- Component rendering
- Hook behavior
- Utility functions

### Integration Tests
- API calls
- User flows
- Error scenarios

### E2E Tests
- Full user journeys
- Cross-browser testing

## Performance Optimizations

1. **React.memo**: Prevent unnecessary re-renders
2. **useCallback**: Stable function references
3. **Code Splitting**: Automatic with Next.js
4. **Image Optimization**: Next.js Image component
5. **Font Optimization**: Google Fonts with Next.js

## Security Considerations

1. **XSS Protection**: React escapes by default
2. **HTTPS**: Production deployment
3. **Environment Variables**: Sensitive data protection
4. **CORS**: Backend handles CORS
5. **Input Validation**: Client and server-side

## Deployment

### Build Process
```bash
npm run build
npm start
```

### Environment
- **Development**: `npm run dev`
- **Production**: `npm run build && npm start`
- **Type Check**: `npm run type-check`

### Hosting Options
- **Vercel**: Recommended (Next.js creators)
- **Netlify**: Alternative
- **AWS Amplify**: Enterprise option
- **Docker**: Containerized deployment

## Future Enhancements

1. **Internationalization**: Multi-language support
2. **Dark Mode**: Theme switching
3. **Offline Support**: PWA capabilities
4. **Analytics**: User behavior tracking
5. **A/B Testing**: Feature experimentation
6. **Caching**: API response caching
7. **Pagination**: For large result sets
8. **Bookmarking**: Save favorite guidance
9. **Sharing**: Social media integration
10. **Audio**: Quran recitation playback

## Code Standards

### Naming Conventions
- **Components**: PascalCase (`GuidanceCard.tsx`)
- **Hooks**: camelCase with `use` prefix (`useGuidance.ts`)
- **Constants**: UPPER_SNAKE_CASE (`API_CONFIG`)
- **Functions**: camelCase (`fetchGuidance`)

### File Organization
- One component per file
- Co-locate related files
- Index files for clean imports
- Separate concerns (UI, logic, data)

### Comments
- JSDoc for public APIs
- Inline comments for complex logic
- TODO comments for future work
- No obvious comments

## Maintenance

### Dependencies
- Regular updates via `npm update`
- Security audits via `npm audit`
- Breaking changes review
- Lock file commits

### Code Review
- TypeScript errors: Zero tolerance
- ESLint warnings: Address all
- Accessibility: WCAG 2.1 AA
- Performance: Lighthouse score > 90
