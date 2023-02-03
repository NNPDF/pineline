import type { DocsThemeConfig } from 'nextra-theme-docs'
import getConfig from 'next/config';
import { useRouter } from 'next/router'

const logo = (
    <>
        <span style={{ fontWeight: 800, marginRight: "0.5rem" }}>Pineline</span>
        <span style={{ fontWeight: 400, color: "rgb(75 85 99/var(--tw-text-opacity))" }}>
            Theory predictions for PDF fitting
        </span>
        <style jsx>{`
          span {
            display: none;
          }

          @media (min-width: 768px) { 
            span {
              display: inline;
            }
          }
        `}
        </style>
    </>
)

const head = () => (
    <>
        <meta name="msapplication-TileColor" content="#ffffff" />
        <meta name="theme-color" content="#ffffff" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta httpEquiv="Content-Language" content="en" />
        <meta name="description" content="Nextra: the Next.js site builder" />
        <meta name="og:description" content="Nextra: the Next.js site builder" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:image" content="https://nextra.vercel.app/og.png" />
        <meta name="twitter:site:domain" content="nextra.vercel.app" />
        <meta name="twitter:url" content="https://nextra.vercel.app" />
        <meta name="og:title" content="Nextra: Next.js static site generator" />
        <meta name="og:image" content="https://nextra.vercel.app/og.png" />
        <meta name="apple-mobile-web-app-title" content="Nextra" />
        <link
            rel="apple-touch-icon"
            sizes="180x180"
            href={process.env.basePath + '/apple-icon-180x180.png'}
        />
        <link
            rel="icon"
            type="image/png"
            sizes="192x192"
            href={process.env.basePath + '/android-icon-192x192.png'}
        />
        <link
            rel="icon"
            type="image/png"
            sizes="32x32"
            href={process.env.basePath + '/favicon-32x32.png'}
        />
        <link
            rel="icon"
            type="image/png"
            sizes="96x96"
            href={process.env.basePath + '/favicon-96x96.png'}
        />
        <link
            rel="icon"
            type="image/png"
            sizes="16x16"
            href={process.env.basePath + '/favicon-16x16.png'}
        />
        <meta
            name="msapplication-TileImage"
            content={process.env.basePath + '/ms-icon-144x144.png'}
        />
    </>
)

export default {
    project: {
        link: 'https://github.com/NNPDF/pineline'
    },
    docsRepositoryBase: 'https://github.com/NNPDF/pineline/',
    editLink: {
        text: 'Edit this page on GitHub'
    },
    logo,
    head,
    navigation: {
        prev: true,
        next: true
    },
    toc: {
        float: true
    },
    sidebar: {
        defaultMenuCollapseLevel: 1,
        titleComponent: ({ title }) => <>{title}</>
    },
    footer: {
        text: <>{new Date().getFullYear()} © N3PDF.</>
    },
    useNextSeoProps() {
        const { asPath } = useRouter()

        const { basePath } = getConfig()
        const suffix = asPath !== basePath ? '' : ' - Pineline'
        return {
            titleTemplate: `%s${suffix}`
        }
    },
} as DocsThemeConfig
