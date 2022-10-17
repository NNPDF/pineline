import type { ReactElement } from 'react'
import type { AppProps } from 'next/app'

import Prism from 'prismjs'

import 'nextra-theme-docs/style.css'
import '../style/highlight.css'

export default function Nextra({
  Component,
  pageProps,
}: AppProps): ReactElement {
  // Use the layout defined at the page level, if available
  // const getLayout = Component.getLayout || ((page) => page)

  return <Component {...pageProps} />
}

;(typeof global !== 'undefined' ? global : window).Prism = Prism
require('prismjs/components/prism-toml')
