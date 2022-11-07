import styles from './internal-link.module.css'

export default function ({ href, children }) {
  return (
    <a href={href} className={styles.link}>
      {children}
    </a>
  )
}
