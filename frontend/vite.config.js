import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    // Onde os arquivos de produção serão gerados
    outDir: '../static/dist',
    manifest: true,
    rollupOptions: {
      // O arquivo de entrada para o build de produção
      input: 'src/main.jsx',
    }
  },
  server: {
    port: 5173,
  }
})
