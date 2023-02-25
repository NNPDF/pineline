import Link from 'next/link';

import styles from './internal-link.module.css'

export default function ({ href, children }) {
  return (
    <Link href={href}>
      <a className={styles.link}>{children}</a>
    </Link>
  )
}
