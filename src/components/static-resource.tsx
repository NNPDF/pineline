import InternalLink from './internal-link'
import GHLink from './gh-link'

export default function ({ href, children }) {
  return <>
      <InternalLink href={href}>{children}</InternalLink>
      <GHLink href={"public" + href}/>
    </>
}
