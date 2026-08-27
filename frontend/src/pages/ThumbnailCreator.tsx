import React from 'react';
import { PhotoIcon } from '@heroicons/react/24/solid';

const ThumbnailCreator: React.FC = () => {
  return (
    <div className="space-y-6">
      <div className="flex items-center space-x-3">
        <PhotoIcon className="w-8 h-8 text-primary-500" />
        <h1 className="text-2xl md:text-3xl font-bold text-dark-50">Thumbnail Creator</h1>
      </div>

      <div className="bg-dark-800 rounded-lg border border-dark-700 p-6">
        <h2 className="text-lg font-semibold text-dark-50 mb-4">AI Thumbnail Generator</h2>
        <p className="text-dark-400 mb-6">Generate eye-catching thumbnails using AI</p>
        <button className="btn-primary">Create Thumbnail</button>
      </div>
    </div>
  );
};

export default ThumbnailCreator;
