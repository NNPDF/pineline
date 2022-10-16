import 'nextra-theme-docs/style.css'
import '../style/highlight.css'
import Prism from 'prism-react-renderer/prism'

export default function Nextra({ Component, pageProps }) {
  // Use the layout defined at the page level, if available
  const getLayout = Component.getLayout || ((page) => page)

  return getLayout(<Component {...pageProps} />)
}

;(typeof global !== 'undefined' ? global : window).Prism = Prism
require('prismjs/components/prism-toml')
