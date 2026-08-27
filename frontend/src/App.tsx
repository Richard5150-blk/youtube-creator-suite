import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Toaster } from 'react-hot-toast';
import Layout from '@/components/Layout';
import Dashboard from '@/pages/Dashboard';
import Analytics from '@/pages/Analytics';
import VideoGenerator from '@/pages/VideoGenerator';
import ThumbnailCreator from '@/pages/ThumbnailCreator';
import VoiceGenerator from '@/pages/VoiceGenerator';
import VideoRenderer from '@/pages/VideoRenderer';
import Login from '@/pages/Login';
import NotFound from '@/pages/NotFound';

function App(): JSX.Element {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route
          element={<Layout />}
        >
          <Route path="/" element={<Dashboard />} />
          <Route path="/analytics" element={<Analytics />} />
          <Route path="/videos/generate" element={<VideoGenerator />} />
          <Route path="/thumbnails" element={<ThumbnailCreator />} />
          <Route path="/voice" element={<VoiceGenerator />} />
          <Route path="/render" element={<VideoRenderer />} />
          <Route path="*" element={<NotFound />} />
        </Route>
      </Routes>
      <Toaster position="bottom-center" />
    </Router>
  );
}

export default App;
