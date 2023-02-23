import type { DocsThemeConfig } from 'nextra-theme-docs'
import getConfig from 'next/config';
import { useRouter } from 'next/router'

const logo = (
    <>
        <span style={{ fontWeight: 800, marginRight: "0.5rem" }}>Pineline</span>
        <span className="subtitle" style={{ fontWeight: 400, color: "rgb(75 85 99/var(--tw-text-opacity))" }}>
            Theory predictions for PDF fitting
        </span>
        <style jsx>{`
          .subtitle {
            display: none;
          }

          @media (min-width: 768px) { 
            .subtitle {
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
        <meta name="description" content="Pineline - high-energy theory predictions" />
        <meta name="og:description" content="Pineline - high-energy theory predictions" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:image" content="https://raw.githubusercontent.com/NNPDF/pineline/main/public/pineline.svg" />
        <meta name="twitter:site:domain" content="nnpdf.github.io" />
        <meta name="twitter:url" content="https://nnpdf.github.io/pineline" />
        <meta name="og:title" content="Pineline - high-energy theory predictions" />
        <meta name="og:image" content="https://raw.githubusercontent.com/NNPDF/pineline/main/public/pineline.svg" />
        <meta name="apple-mobile-web-app-title" content="Pineline" />
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
        text: <>{new Date().getFullYear()} © <span style={{ width: '.3em' }} /><a href="https://n3pdf.mi.infn.it">N3PDF</a></>
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
