import React, { useRef, useEffect, useState } from 'react';

const WaveBackground = () => {
  const canvasRef = useRef(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight * 0.3;

    const baseFrequency = 0.02;
    const baseAmplitude = 50;
    let targetFrequency = baseFrequency;
    let frequency = baseFrequency;
    let targetAmplitude = baseAmplitude;
    let amplitude = baseAmplitude;
    let phase = 0;
    let bounce = 0;

    const waveLayers = [
      { amplitude: baseAmplitude, frequency: baseFrequency, phaseOffset: 0 },
      { amplitude: baseAmplitude * 0.8, frequency: baseFrequency * 1.1, phaseOffset: Math.PI / 4 },
      { amplitude: baseAmplitude * 0.6, frequency: baseFrequency * 1.3, phaseOffset: Math.PI / 2 },
    ];
    //resize

    const handleResize = () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight * 0.3;
    };

    const handleMouseMove = (e) => {
      const xPositionRatio = e.clientX / canvas.width;
      const yPositionRatio = e.clientY / canvas.height;

      targetFrequency = baseFrequency + (1 - xPositionRatio) * 0.05;
      targetAmplitude = baseAmplitude + yPositionRatio * 30;
    };

    //bounce effect on click
    const handleClick = () => {
      bounce = 50;
    };

    window.addEventListener('resize', handleResize);
    window.addEventListener('mousemove', handleMouseMove);
    window.addEventListener('click', handleClick);

    const drawWave = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      frequency += (targetFrequency - frequency) * 0.05;
      amplitude += ((targetAmplitude + bounce) - amplitude) * 0.05;

      if (bounce > 0) {
        bounce *= 0.9;
      }

      waveLayers.forEach(({ amplitude: layerAmplitude, frequency: layerFrequency, phaseOffset }, index) => {
        ctx.beginPath();
        ctx.moveTo(0, canvas.height / 2);

        const offset = canvas.width * 0.1;
        for (let x = -offset; x < canvas.width; x++) {
          const y =
            canvas.height / 2 +
            Math.sin(x * frequency * layerFrequency + phase + phaseOffset) * (amplitude * layerAmplitude / baseAmplitude);
          ctx.lineTo(x, y);
        }


        ctx.strokeStyle = `rgba(255, 255, 255, ${.9 / (index + 1)})`;
        ctx.lineWidth = 2;
        ctx.stroke();
      });

      phase += 0.05;
      requestAnimationFrame(drawWave);
    };

    drawWave();

    return () => {
      window.removeEventListener('resize', handleResize);
      window.removeEventListener('mousemove', handleMouseMove);
      window.removeEventListener('click', handleClick);
    };
  }, []);

  return (
    <canvas
      ref={canvasRef}
      style={{
        position: 'absolute',
        bottom: 0,
        left: 0,
        width: '100%',
        height: '30vh',
        zIndex: 2,
      }}
    />
  );
};

export default WaveBackground;
