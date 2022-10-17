import Head from 'next/head'
import Link from 'next/link'

import Home from '@components/layout'

import styles from '@components/home.module.css'

export default function Page() {
  return (
    <Home>
      <Head>
        <title>Pineline</title>
        <meta name="description" content="Pineline home page" />
      </Head>
      <div className={styles.titlebox}>
        <h1>Pineline</h1>
        <h5>Theory predictions for PDF fitting</h5>
      </div>
      <div className={styles.links}>
        <h3 className={styles.link}>
          <Link href="/introduction">Introduction</Link>
        </h3>
        <h3 className={styles.link}>
          <Link href="/installation">Installation</Link>
        </h3>
        <h3 className={styles.link}>
          <Link href="/tutorials/setup">Tutorials</Link>
        </h3>
      </div>
    </Home>
  )
}
