import { Request, Response, NextFunction } from 'express';
import { logger } from '@/utils/logger';

interface ErrorResponse {
  error: string;
  message: string;
  statusCode: number;
  timestamp: string;
  path?: string;
}

class AppError extends Error {
  constructor(
    public statusCode: number,
    message: string,
    public details?: unknown
  ) {
    super(message);
    Object.setPrototypeOf(this, AppError.prototype);
  }
}

const errorHandler = (
  err: Error | AppError,
  req: Request,
  res: Response,
  next: NextFunction
): void => {
  const statusCode = err instanceof AppError ? err.statusCode : 500;
  const message = err.message || 'Internal Server Error';
  const details = err instanceof AppError ? err.details : undefined;

  const errorResponse: ErrorResponse = {
    error: err.constructor.name,
    message,
    statusCode,
    timestamp: new Date().toISOString(),
    path: req.path
  };

  // Log error
  if (statusCode >= 500) {
    logger.error('Server Error:', { error: err, request: { method: req.method, path: req.path } });
  } else {
    logger.warn('Client Error:', { statusCode, message, path: req.path });
  }

  res.status(statusCode).json(errorResponse);
};

export { AppError, errorHandler };
export default errorHandler;
