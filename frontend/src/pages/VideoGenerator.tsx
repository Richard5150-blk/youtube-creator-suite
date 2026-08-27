import React from 'react';
import { VideoCameraIcon } from '@heroicons/react/24/solid';

const VideoGenerator: React.FC = () => {
  return (
    <div className="space-y-6">
      <div className="flex items-center space-x-3">
        <VideoCameraIcon className="w-8 h-8 text-primary-500" />
        <h1 className="text-2xl md:text-3xl font-bold text-dark-50">Video Generator</h1>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div className="bg-dark-800 rounded-lg border border-dark-700 p-6">
          <h2 className="text-lg font-semibold text-dark-50 mb-4">Long-Form Videos</h2>
          <p className="text-dark-400 mb-4">Create videos up to 30 minutes</p>
          <button className="w-full btn-primary">Generate</button>
        </div>
        <div className="bg-dark-800 rounded-lg border border-dark-700 p-6">
          <h2 className="text-lg font-semibold text-dark-50 mb-4">Short-Form Videos</h2>
          <p className="text-dark-400 mb-4">Create TikTok, Shorts, and Reels</p>
          <button className="w-full btn-primary">Generate</button>
        </div>
      </div>
    </div>
  );
};

export default VideoGenerator;
