import { useRouter } from 'next/router';
import { useEffect, useState } from 'react';

import styles from './avatar.module.css';


export default function({ name }) {
    const router = useRouter();
    const [url, setUrl] = useState(`${router.basePath}/avatar.svg`);

    useEffect(() => {
        (async () => {
            let response = await fetch(`https://api.github.com/users/${name}`);
            let url = (await response.json()).avatar_url;

            setUrl(url);
        })()
    })


    return (
        <img className={styles.pic} src={url} />
    )
}

