import 'express-async-errors';
import express, { Express, Request, Response, NextFunction } from 'express';
import cors from 'cors';
import helmet from 'helmet';
import dotenv from 'dotenv';
import path from 'path';
import { logger } from '@/utils/logger';
import errorHandler from '@/middleware/errorHandler';
import authRoutes from '@/routes/auth.routes';
import analyticsRoutes from '@/routes/analytics.routes';
import videoRoutes from '@/routes/video.routes';
import thumbnailRoutes from '@/routes/thumbnail.routes';
import voiceRoutes from '@/routes/voice.routes';
import renderRoutes from '@/routes/render.routes';

// Load environment variables
dotenv.config();

const app: Express = express();
const PORT = process.env.PORT || 5000;
const NODE_ENV = process.env.NODE_ENV || 'development';

// Security Middleware
app.use(helmet());
app.use(cors({
  origin: process.env.CORS_ORIGIN || 'http://localhost:3000',
  credentials: true
}));

// Body Parser Middleware
app.use(express.json({ limit: '50mb' }));
app.use(express.urlencoded({ limit: '50mb', extended: true }));

// Request Logging Middleware
app.use((req: Request, res: Response, next: NextFunction) => {
  logger.info(`${req.method} ${req.path}`);
  next();
});

// Health Check Endpoint
app.get('/api/health', (req: Request, res: Response) => {
  res.json({
    status: 'ok',
    timestamp: new Date(),
    environment: NODE_ENV
  });
});

// API Routes
app.use('/api/v1/auth', authRoutes);
app.use('/api/v1/analytics', analyticsRoutes);
app.use('/api/v1/videos', videoRoutes);
app.use('/api/v1/thumbnails', thumbnailRoutes);
app.use('/api/v1/voice', voiceRoutes);
app.use('/api/v1/render', renderRoutes);

// 404 Handler
app.use((req: Request, res: Response) => {
  res.status(404).json({
    error: 'Route not found',
    path: req.path,
    method: req.method
  });
});

// Error Handler Middleware (must be last)
app.use(errorHandler);

// Server Startup
const startServer = async (): Promise<void> => {
  try {
    // Initialize database connection
    logger.info('Initializing database connection...');
    // Database initialization code will go here
    
    app.listen(PORT, () => {
      logger.info(`✅ Server running on http://localhost:${PORT}`);
      logger.info(`📡 Environment: ${NODE_ENV}`);
      logger.info(`📚 API docs available at http://localhost:${PORT}/api/docs`);
    });
  } catch (error) {
    logger.error('Failed to start server:', error);
    process.exit(1);
  }
};

startServer();

export default app;
