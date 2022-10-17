import nextra from 'nextra'

const withNextra = nextra({
  theme: 'nextra-theme-docs',
  themeConfig: './src/theme.config.js',
  unstable_staticImage: true,
})

export default {
  ...withNextra(),
  basePath: '/pineline',
  images: { unoptimized: true },
}
