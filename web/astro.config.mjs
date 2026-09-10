// @ts-check
import { defineConfig } from 'astro/config';

export default defineConfig({
  // The built folder has to open by double-clicking `index.html`, with no
  // server. The run it renders is unpublished work on institutional
  // infrastructure, so "send the reviewer a folder" is the distribution
  // method, and a page that only works over http:// is a page that works for
  // everyone except the person you sent it to.
  //
  // Astro emits `/assets/…` regardless of `base`, and an absolute path
  // resolves against the filesystem root when a page is opened as a file — the
  // page loads unstyled and inert. So asset URLs are made relative after the
  // build, by scripts/relativise.mjs.
  build: { assets: 'assets', format: 'file' },
  vite: {
    build: {
      // Nothing inlined as a data URI: the same reason. An inlined asset is
      // fine, but the threshold means some assets inline and some don't, and
      // only the ones that didn't break — which is the kind of bug that ships.
      assetsInlineLimit: 0,
      rollupOptions: {
        output: {
          // Astro's default names a chunk after the module graph that produced
          // it. The hash stays: it is what lets assets cache forever while the
          // page, which carries the data, must not.
          entryFileNames: 'assets/app.[hash].js',
          assetFileNames: 'assets/[name].[hash][extname]',
        },
      },
    },
  },
});
