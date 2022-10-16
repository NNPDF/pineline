// pages/index.js

import Layout from '../components/layout.tsx'
import NestedLayout from '../components/nested-layout.tsx'

import styles from '../components/home.module.css'

export default function Page() {
  return (
    <>
      <div className={styles.titlebox}>
        <h1>Home</h1>
      </div>
      <div className={styles.links}>
        <h3 className={styles.link}>
          <a href="/introduction">Introduction</a>
        </h3>
        <h3 className={styles.link}>
          <a href="/installation">Installation</a>
        </h3>
        <h3 className={styles.link}>
          <a href="/tutorials">Tutorials</a>
        </h3>
      </div>
    </>
  )
}

Page.getLayout = function getLayout(page) {
  return (
    <Layout>
      <NestedLayout>{page}</NestedLayout>
    </Layout>
  )
}
