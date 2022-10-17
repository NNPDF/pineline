import type { ReactElement } from 'react'
import type { AppProps } from 'next/app'

import Prism from 'prismjs'

import '../style/style.css'
import '../style/highlight.css'

export default function Nextra({
  Component,
  pageProps
}: AppProps): ReactElement {
  return <Component {...pageProps} />
}

;(typeof global !== 'undefined' ? global : window).Prism = Prism
require('prismjs/components/prism-toml')
