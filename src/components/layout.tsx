import styles from './layout.module.css'

export default function Layout({ children }) {
  return <div className={styles.center}>{children}</div>
}
