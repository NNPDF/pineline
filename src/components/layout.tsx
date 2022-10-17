import styles from './layout.module.css'

export default function ({ children }) {
  return <div className={styles.center}>{children}</div>
}
