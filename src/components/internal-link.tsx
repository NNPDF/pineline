import { useRouter } from 'next/router';
import Link from 'next/link';

import styles from './internal-link.module.css'

export default function ({ href, children }) {
  const router = useRouter();

  return (
    <Link href={`${router.basePath}/${href}`}>
      <a className={styles.link}>{children}</a>
    </Link>
  )
}
