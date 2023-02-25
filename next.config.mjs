import nextra from 'nextra'

const withNextra = nextra({
  theme: 'nextra-theme-docs',
  themeConfig: './src/theme.config.tsx',
  staticImage: true,
  flexsearch: {
    codeblocks: true
  },
  latex: true,
  defaultShowCopyCode: true
})

export default {
  ...withNextra({
    reactStrictMode: true
  }),
  basePath: '/pineline',
  paths: {
    "@components/*": ["components/*"]
  },
  env: {
    basePath: '/pineline'
  },
  images: {
    unoptimized: true
  }
}
